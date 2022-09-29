from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from main_window_ui import Ui_MainWindow
Form, Window = uic.loadUiType("UI.ui")

app = QApplication([])
window = Ui_MainWindow()
window.show()
app.exec()
#PyUic или писать кнопки руками