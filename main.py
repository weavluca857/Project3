import sys
import time
from parse import *
from Insertion import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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

        y = s[0:len(s)]
        #if str(self.comboBox.currentText()) == 'latitude':
        tic = time.perf_counter()
        #insertion_sort_latitude(s)
        toc = time.perf_counter()
        #self.l1.setText(f"Finished Insertion sort in {toc - tic:0.4f} seconds")
        QMessageBox.question(self, 'insertion sort',f"Finished Insertion sort in {toc - tic:0.4f} seconds", QMessageBox.Ok, QMessageBox.Ok)
        tic = time.perf_counter()
        shell_sort_latitude(y)
        toc = time.perf_counter()
        #(f"Finished Shell sort in {toc - tic:0.4f} seconds")
        QMessageBox.question(self,'shell sort', f"Finished Shell sort in {toc - tic:0.4f} seconds", QMessageBox.Ok, QMessageBox.Ok)
        #else:
        #    insertion_sort_longitude(s)
        #    shell_sort_longitude(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()