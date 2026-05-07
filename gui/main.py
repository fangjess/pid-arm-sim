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
                    visibility = 1.0 # full visibility if no rotation
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
        self.setWindowTitle("pid-arm-sim")

        # create arm
        self.arm = arm_sim.Arm()
        self.arm.addJoint(arm_sim.Joint())  # horizontal base joint
        self.arm.addJoint(arm_sim.Joint())  # vertical joint
        self.arm.toggleAxis(1)    
        self.arm.setTarget(0, 45.0)         # rotate base 45°
        self.arm.setTarget(1, 30.0)         # pitch vertical joint up 30°

        # canvases
        self.sideCanvas = SideViewCanvas(self.arm)
        self.sideCanvas.setFixedSize(450, 500)
        self.topCanvas = TopViewCanvas(self.arm)
        self.topCanvas.setFixedSize(450, 500)

        # layout
        layout = QHBoxLayout()
        layout.addWidget(self.sideCanvas)
        layout.addWidget(self.topCanvas)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(16)

    def tick(self):
        self.arm.step(0.001)
        self.sideCanvas.update()
        self.topCanvas.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())