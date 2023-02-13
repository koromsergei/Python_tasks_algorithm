import sys
#import pytest
#from trim import TRIMScanner
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from TRIM import TRIMScanner

sc = TRIMScanner(ip="127.0.0.1", port=9000)
sc.connect()

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # разрешает Qt настраивать объект
        self.setWindowTitle("My App")
        button = QPushButton("Launch the scanner!")
        #self.setFixedSize(QSize(1000, 600))
        self.setMinimumSize(QSize(1000, 600))
        self.setCentralWidget(button) # Устанавливаем центральный виджет Window.
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)


    def the_button_was_clicked(self):

     print("The scanner is launched!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()