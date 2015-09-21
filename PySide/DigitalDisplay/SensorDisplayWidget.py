'''
CoroBot Digital Display for Sensor Data
Developer: CoroWare
Date: 30, September 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''
import sys
from PySide import QtCore, QtGui

class DigitalDisplay(QtGui.QWidget):
    def __init__(self,parent, sensor_name='Sensor',Units='cm'):
        QtGui.QWidget.__init__(self)
        self.sensor_name = sensor_name
        palette = self.palette()
#         if sensor_value >= x:
#             palette.setColor(palette.WindowText,QtGui.QColor(0,255,0))
#         elif x > sensor_value > y:
#             palette.setColor(palette.WindowText,QtGui.QColor(255,255,0))
#         elif sensor_value <= y:
#             palette.setColor(palette.WindowText, QtGui.QColor(255,0,0))

        palette.setColor(palette.WindowText,QtGui.QColor(255,0,0))

        #Needs case structure depending on incoming signal to change number value colors from green to yellow to red depending on a range of distances

        self.displayname= QtGui.QLabel(self.sensor_name)
        self.sensordisplay = QtGui.QLCDNumber(self)
        self.sensordisplay.setDigitCount(4)
        self.setPalette(palette)


        displayLayout = QtGui.QGridLayout(self)
#          displayLayout.addWidget(self.displayname, 0, 0)
        displayLayout.addWidget(self.sensordisplay, 0,0)

        self.setLayout(displayLayout)
