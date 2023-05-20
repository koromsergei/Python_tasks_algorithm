import sys
from PyQt6.QtCore    import *
from PyQt6.QtGui     import *
from PyQt6.QtWidgets import *
import pyqtgraph as pg

class Example(QWidget):
    def __init__(self):
        super().__init__()
        button1 = QRadioButton()
        button2 = QPushButton()
        button3 = QRadioButton()


        splitter0 = QSplitter(orientation=Qt.Orientation.Horizontal)

        splitter1 = QSplitter(orientation=Qt.Orientation.Vertical)
        splitter1.insertWidget(0, pg.plot())
        splitter2 = QSplitter(orientation=Qt.Orientation.Vertical)
        splitter2.insertWidget(0, button2)

        splitter0.insertWidget(0, splitter1)
        splitter0.insertWidget(1, splitter2)
        hbox = QHBoxLayout(self)
        hbox.addWidget(splitter0)
        self.setLayout(hbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.setGeometry(300, 300, 900, 600)
    ex.setWindowTitle('QSplitter demo')
    ex.show()
    sys.exit(app.exec())
