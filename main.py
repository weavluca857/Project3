import sys
from parse import *
from Insertion import *
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QComboBox, QPushButton
from PyQt5.QtCore import Qt

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Project 3")
        self.setGeometry(50, 50, 500, 300)

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        mainMenu = self.menuBar()

        self.home()

    def home(self):
        self.comboBox = QComboBox(self)
        self.comboBox.addItem('Latitude')
        self.comboBox.addItem('Longitude')
        self.comboBox.move(20, 20)

        self.pb = QPushButton(self)
        self.pb.setText('Run')
        self.pb.move(20, 250)
        self.pb.clicked.connect(self.run)
    def run(self):
        s = parse('/Users/lucas/worldcitiespop.csv')
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()