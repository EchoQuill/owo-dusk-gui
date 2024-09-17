import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap
from interface import Ui_owoDusk
from PySide6.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_owoDusk()
        self.ui.setupUi(self)

        # Set initial page
        self.ui.stackedWidget.setCurrentIndex(0)
        # Connect buttons to switch pages
        self.ui.homebtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.accountsbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.settingsbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.commandsbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.aboutbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))

        # Access the QLabel widget directly
        self.label = self.ui.logo
        self.label.setScaledContents(True)

        # Load and set the image
        pixmap = QPixmap('owo-dusk.png')
        if pixmap.isNull():
            print("Failed to load image")
        else:
            scaled_pixmap = pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label.setPixmap(scaled_pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
