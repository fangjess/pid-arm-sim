import sys
import os
import math
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

sys.path.append(os.path.join(os.path.dirname(__file__), "../build"))
import arm_sim

# class TopViewCanvas(QWidget):
#     def paintEvent(self, event):
#         painter = QPainter(self)
#         sx = self.width()
#         sy = self.height()
#         self.drawArm(painter, sx, sy)

#     def drawArm(self, painter, startX, startY):


class SideViewCanvas(QWidget):
    def __init__(self, arm):
        super().__init__()
        self.arm = arm
        self.scale = 300 # 1 metre = 300 pixels     

    def paintEvent(self, event):
        painter = QPainter(self)
        sx = self.width() // 2
        sy = self.height() // 2
        self.drawArm(painter, sx, sy)

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



class MainWindow(QMainWindow):

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()