import sys
import os
import math
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

sys.path.append(os.path.join(os.path.dirname(__file__), "../build"))
import arm_sim

class SideViewCanvas(QWidget):
    def __init__(self, arm):
        super().__init__()
        self.arm = arm
        self.scale = 300 # 1 metre = 300 pixels     

    def paintEvent(self, event):
        painter = QPainter(self)
        sx = self.width() // 2
        sy = self.height() - 50
        self.drawSide(painter, sx, sy)

    def drawSide(self, painter, startX, startY):
        x1, y1 = startX, startY
        accumulatedRotation = 0.0 # tracking accumulated horizontal rotation for foreshortening
        attachedHorizontal = False # tracks if current joint is above a horizontal one to trigger foreshortening

        for i in range(self.arm.getJointCount()):
            angleRad = math.radians(self.arm.getAngle(i))
            length = self.arm.getLength(i) * self.scale
            axis = self.arm.getAxis(i)

            if axis == arm_sim.Axis.Horizontal:
                attachedHorizontal = True
                accumulatedRotation += angleRad
                x2 = x1 # horizontal axis arms are just a straight pole from the side
                y2 = y1 - length

            else:
                if attachedHorizontal:
                    visibility = math.cos(accumulatedRotation)
                else:
                    visibility = 1.0
                x2 = x1 + length * math.cos(angleRad) * visibility 
                y2 = y1 - length * math.sin(angleRad)


            painter.drawLine(int(x1), int(y1), int(x2), int(y2))
            painter.drawEllipse(int(x1) - 4, int(y1) - 4, 8, 8)
            x1, y1 = x2, y2

        painter.drawEllipse(int(x1) - 4, int(y1) - 4, 8, 8)

class TopViewCanvas(QWidget):
    def __init__(self, arm):
        super().__init__()
        self.arm = arm
        self.scale = 300 # 1 metre = 300 pixels
    
    def paintEvent(self, event):
        painter = QPainter(self)
        sx = self.width() // 2
        sy = self.height() // 2
        self.drawTop(painter, sx, sy)

    def drawTop(self, painter, startX, startY):
        x1, y1 =  startX, startY
        accumulatedRotation = 0.0

        for i in range(self.arm.getJointCount()):
            angleRad = math.radians(self.arm.getAngle(i))
            length = self.arm.getLength(i) * self.scale
            axis = self.arm.getAxis(i)

            if axis == arm_sim.Axis.Horizontal:
                accumulatedRotation += angleRad
                painter.drawEllipse(int(x1) - 4, int(y1) - 4, 8, 8)

            else:
                foreshortened = length * math.cos(angleRad)
                x2 = x1 + foreshortened * math.cos(accumulatedRotation)
                y2 = y1 - foreshortened * math.sin(accumulatedRotation)
                painter.drawLine(int(x1), int(y1), int(x2), int(y2))
                painter.drawEllipse(int(x1) - 4, int(y1) - 4, 8, 8)
                x1, y1 = x2, y2
            
        painter.drawEllipse(int(x1) - 4, int(y1) - 4, 8, 8)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 600)
        self.setWindowTitle("PID Robotic Arm Simulator")
        self.MAX_JOINTS = 5
        self.jointPanels = []

        # create arm object
        self.arm = arm_sim.Arm()

        # canvases
        self.sideCanvas = SideViewCanvas(self.arm)
        self.sideCanvas.setFixedSize(450, 500)
        self.topCanvas = TopViewCanvas(self.arm)
        self.topCanvas.setFixedSize(450, 500)

        # canvas layout
        sideLayout = QHBoxLayout()
        sideLayout.addWidget(self.sideCanvas)
        sideCanvasGroup = QGroupBox("Side View")
        sideCanvasGroup.setLayout(sideLayout)

        topLayout = QHBoxLayout()
        topLayout.addWidget(self.topCanvas)
        topCanvasGroup = QGroupBox("Top View")
        topCanvasGroup.setLayout(topLayout)

        canvasLayout = QHBoxLayout()
        canvasLayout.addWidget(sideCanvasGroup)
        canvasLayout.addWidget(topCanvasGroup)

        # control panel layout
        self.controlLayout = QVBoxLayout()
        self.controlLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        scrollWidget = QWidget()
        scrollWidget.setLayout(self.controlLayout)

        scrollPanel = QScrollArea()
        scrollPanel.setWidget(scrollWidget)
        scrollPanel.setWidgetResizable(True)
        scrollPanel.setFixedWidth(250)
        
        # spinbox for adding/removing joints
        self.jointAdder = QSpinBox()
        self.jointAdder.setSuffix(" Joint(s)")
        self.jointAdder.setRange(0, self.MAX_JOINTS)
        self.jointAdder.setValue(2)
        self.jointAdder.valueChanged.connect(self.onJointCountChange)
        self.controlLayout.addWidget(self.jointAdder)

        # initial setup
        self.addJoint()
        self.addJoint()
        self.arm.toggleAxis(1)
        self.jointPanels[1].findChild(QPushButton).setText("Vertical Axis")
        self.arm.setTarget(0, 45.0) # rotate base 45 deg
        self.arm.setTarget(1, 30.0) # pitch vertical joint up 30 deg
        self.jointPanels[0].targetSlider.setValue(45)
        self.jointPanels[1].targetSlider.setValue(30)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(canvasLayout)
        mainLayout.addWidget(scrollPanel)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

        # update canvas
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(16)

    def onTargetChange(self, index, target, label):
        self.arm.setTarget(index, float(target))
        label.setText(f"Target: {target}°")
    
    def onAxisChange(self, index, button):
        self.arm.toggleAxis(index)
        axis = self.arm.getAxis(index)
        if axis == arm_sim.Axis.Horizontal:
            button.setText("Horizontal Axis")
        else:
            button.setText("Vertical Axis")

    def onKpChange(self, index, val, label):
            kp = val / 100.0  # convert to float
            self.arm.setKp(index, kp)
            label.setText(f"Kp: {kp:.2f}")

    def createJointPanel(self, index):
        group = QGroupBox(f"Joint {index}")
        layout = QVBoxLayout()

        # axis toggle button
        axis = self.arm.getAxis(index)
        axisLabel = "Vertical Axis" if axis == arm_sim.Axis.Vertical else "Horizontal Axis"
        axisButton = QPushButton(axisLabel)
        axisButton.clicked.connect(
            lambda checked, i=index, btn=axisButton: self.onAxisChange(i, btn)
        )
        layout.addWidget(axisButton)

        # target angle slider
        target = self.arm.getTarget(index)
        targetLabel = QLabel(f"Target: {int(target)}°")
        targetSlider = QSlider(Qt.Orientation.Horizontal)
        targetSlider.setMinimum(-179)
        targetSlider.setMaximum(179)
        targetSlider.setSingleStep(1)
        targetSlider.setValue(int(target))
        targetSlider.valueChanged.connect(
            lambda val, i=index, l=targetLabel: self.onTargetChange(i, val, l)
        )
        layout.addWidget(targetLabel)
        layout.addWidget(targetSlider)

        # Kp gain slider, must scale
        currentKp = self.arm.getKp(index)
        kpLabel = QLabel(f"Kp multiplier: {float(currentKp)}")
        kpSlider = QSlider(Qt.Orientation.Horizontal)
        kpSlider.setMinimum(0)
        kpSlider.setMaximum(500)
        kpSlider.setSingleStep(5)
        kpSlider.setValue(int(currentKp * 100))  # convert float to int scale
        kpSlider.valueChanged.connect(
            lambda val, i=index, l=kpLabel: self.onKpChange(i, val, l)
        )
        layout.addWidget(kpLabel)
        layout.addWidget(kpSlider)

        group.setLayout(layout)
        group.targetSlider = targetSlider
        group.axisButton = axisButton
        return group

    def addJoint(self):
        currentJointCount = self.arm.getJointCount()
        if currentJointCount >= 5:
            return
        else:
            self.arm.addNewJoint()
            newPanel = self.createJointPanel(currentJointCount)
            self.jointPanels.append(newPanel)
            self.controlLayout.addWidget(newPanel)


    def popJoint(self):
        currentJointCount = self.arm.getJointCount()
        if currentJointCount <= 0:
            return
        else:
            self.arm.popJoint()
            poppedPanel = self.jointPanels.pop()
            self.controlLayout.removeWidget(poppedPanel)
            poppedPanel.deleteLater()

    def onJointCountChange(self, count):
        current = self.arm.getJointCount()
        if current < count:
            for i in range(count - current):
                self.addJoint()
        else:
            for i in range(current - count):
                self.popJoint()

    def tick(self):
        self.arm.step(0.001)
        self.sideCanvas.update()
        self.topCanvas.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())