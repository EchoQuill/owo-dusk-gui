# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QCoreApplication

# Import the generated UI code
from interface import Ui_owoDusk

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_owoDusk()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.homebtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.accountsbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.settingsbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        #print(type(self.ui.Commands))
        self.ui.commandsbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.aboutbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

