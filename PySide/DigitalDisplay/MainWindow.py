'''Testing Git'''

'''
CoroBot Spark Main User Window
Developer: CoroWare
Date: 30, September 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''
import sys
from PySide import QtCore, QtGui
from code import InteractiveConsole
from MenuBar import MainMenuBar
from CameraPortal import VideoDisplayPort
from FourDirectionButtonWidget import DirectionalButtons
from SensorDisplayWidget import DigitalDisplay
from UnitRadioButton import UnitRadioWidget
from iPythonWidget import iPythonTerminalWidget

#Import required modules


class MainUserWindow(QtGui.QMainWindow):
    ''' Main User Window Class, to be the "home" for all widgets'''

    #Constructor Function
    def __init__(self):
        '''Initialization of the Object creates a window with provided dimensions and constraints'''
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle("Spark Control: Python")
        self.setGeometry(1080,500,1080,500) #(x position of center, y position of center, width and height of window)
        self.setMinimumHeight(500)
        self.setMinimumWidth(1080)

#    def setIcon(self):
#        '''Self Explainatory: Sets the icon for the application'''
#        SparkIcon = QtGui.QIcon('icon2.png') #Make Sure to store icon.png file in same folder as MainUserWindow Script
#        self.setWindowIcon(SparkIcon)

    def CenterMethod(self):
        '''Method that centers the application on the computer's main display'''
        #Downside of PySide is there is no self.center method of the widget
        #For discussion of this please visit the SparkForum/PySideDevelopment
        qRect=self.frameGeometry()
        centerPoint =QtGui.QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def CreateStatusBar(self):
        '''Method that creates the status bar. This UI object is used to display general
        information at the bottom of the UI window'''
        self.mainStatusBar = QtGui.QStatusBar()
        self.mainStatusBar.showMessage("Welcome to Spark Control", 3000)
        self.setStatusBar(self.mainStatusBar)
    def SetCentralWidget(self):
        '''Creates central video portal. Video Portal takes one input for
        the color mode to be displayed. The available options are
        RGB = Red, Green, Blue
        GRAY = Grey/Gray depending on nationality
        '''
        self.videoPortal = VideoDisplayPort(self, 'RGB')
        self.setCentralWidget(self.videoPortal)

    def CreateDockWidgets(self):
        '''Method creates the dockable widgets within the window. Within this method is a description
        of the actual widgets being created; instances of button panels and etc.'''

        dock = QtGui.QDockWidget('Motion Control', self)
        dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea | QtCore.Qt.BottomDockWidgetArea)

        self.driveButtons = DirectionalButtons(self,'Forward', 'Right', 'Reverse', 'Left', 'Duty Cycle')
        dock.setWidget(self.driveButtons)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea,dock)


        dock =QtGui.QDockWidget('Camera Control', self)
        self.cameraButtons=DirectionalButtons(self, 'Up', 'Right', 'Down', 'Left', 'Sensitivity')
        dock.setWidget(self.cameraButtons)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea,dock)

        dock = QtGui.QDockWidget("Units",self)
        self.unitDisplay = UnitRadioWidget(self)
        dock.setWidget(self.unitDisplay)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea,dock)


        dock = QtGui.QDockWidget('Front IR Sensor', self)
        self.frontInfrarredSensor = DigitalDisplay(self,'Front IR Sensor', 'cm')
        dock.setWidget(self.frontInfrarredSensor)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)

        dock = QtGui.QDockWidget('Front Left Ultrasonic Sensor', self)
        self.frontLeftUltrasonicSensor = DigitalDisplay(self, 'Front Left Ultrasonic', 'cm')
        dock.setWidget(self.frontLeftUltrasonicSensor)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)

        dock = QtGui.QDockWidget('Front Right Ultrasonic Sensor', self)
        self.frontRightUltrasonicSensor = DigitalDisplay(self,'Front Right Ultrasonic', 'cm')
        dock.setWidget(self.frontRightUltrasonicSensor)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)

        dock = QtGui.QDockWidget('Rear Ultrasonic Sensor', self)
        self.rearUltrasonicSensor = DigitalDisplay(self, 'Rear Ultrasonic', 'cm')
        dock.setWidget(self.rearUltrasonicSensor)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, dock)

        dock = QtGui.QDockWidget('iPython Console',self)
        self.TerminalWidget=iPythonTerminalWidget(self)
        dock.setWidget(self.TerminalWidget)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, dock)


if __name__ == '__main__':
    '''It is best practice to use this type of wrapper to in the event that someone else
    uses your code and has this as an import'''
            # Exception Handling

    try:
        SparkControl = QtGui.QApplication(sys.argv)
        mainWindow = MainUserWindow()
        mainWindow.SetCentralWidget()
        mainWindow.CreateDockWidgets()
#        mainWindow.setIcon()
        mainWindow.CreateStatusBar()
        SparkMenu = MainMenuBar()
        SparkMenu.SetupComponents()
        mainWindow.setMenuBar(SparkMenu)
        mainWindow.CenterMethod()
        mainWindow.show()
        SparkControl.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print (sys.exc_info()[1])
