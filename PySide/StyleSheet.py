from PySide import QtCore, QtGui

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.edit = QtGui.QLineEdit(self)
        self.edit.setProperty('warning', False)
        self.edit.setStyleSheet("""
           /* other rules go here */
           QLineEdit[warning="true"] {background-color: yellow};
           QLineEdit[warning="false"] {background-color: palette(base)};
            """)
        self.button = QtGui.QPushButton('Test', self)
        self.button.clicked.connect(self.handleButton)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

    def handleButton(self):
        self.edit.setProperty(
            'warning', not self.edit.property('warning'))
        self.edit.style().unpolish(self.edit)
        self.edit.style().polish(self.edit)

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
