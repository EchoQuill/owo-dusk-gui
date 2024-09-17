# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_owoDusk(object):
    def setupUi(self, owoDusk):
        if not owoDusk.objectName():
            owoDusk.setObjectName(u"owoDusk")
        owoDusk.resize(784, 603)
        self.centralwidget = QWidget(owoDusk)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QMainWindow {\n"
"	color: green;\n"
"	background-color: black;\n"
"	border: 1px solid #7600d1;\n"
"}\n"
"QWidget {\n"
"    background-color: black;\n"
"    border: 1px solid #7600d1;\n"
"	color: #ff87ff;\n"
"}\n"
"QFrame {\n"
"    background-color: #11061c;\n"
"    border: 1px solid #691ca3;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton {\n"
"	border-radius:9px;\n"
"}\n"
"Spacer {\n"
"	border: none;\n"
"}\n"
"QStackedWidget {border:none;}\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.accountFrame = QFrame(self.centralwidget)
        self.accountFrame.setObjectName(u"accountFrame")
        self.accountFrame.setStyleSheet(u"QPushButton {\n"
"	border-radius:13px;\n"
"	padding:12px\n"
"}")
        self.accountFrame.setFrameShape(QFrame.StyledPanel)
        self.accountFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.accountFrame)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 3, 15, 3)
        self.homebtn = QPushButton(self.accountFrame)
        self.homebtn.setObjectName(u"homebtn")

        self.horizontalLayout_2.addWidget(self.homebtn)

        self.accountsbtn = QPushButton(self.accountFrame)
        self.accountsbtn.setObjectName(u"accountsbtn")

        self.horizontalLayout_2.addWidget(self.accountsbtn)

        self.settingsbtn = QPushButton(self.accountFrame)
        self.settingsbtn.setObjectName(u"settingsbtn")

        self.horizontalLayout_2.addWidget(self.settingsbtn)

        self.commandsbtn = QPushButton(self.accountFrame)
        self.commandsbtn.setObjectName(u"commandsbtn")

        self.horizontalLayout_2.addWidget(self.commandsbtn)


        self.verticalLayout_2.addWidget(self.accountFrame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 15, 0, 0)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")

        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"    background-color: #11061c;\n"
"    border: 1px solid #691ca3;\n"
"    border-radius: 10px;\n"
"	padding: 2px;\n"
"}\n"
"")
        self.label.setMidLineWidth(0)
        self.label.setMargin(0)
        self.label.setOpenExternalLinks(False)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 39)

        self.horizontalLayout.addWidget(self.frame_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QWidget {border-radius:10px}")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.gridLayout_2 = QGridLayout(self.Home)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.Home)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.Home)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_2.addWidget(self.textBrowser, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 10)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.stackedWidget.addWidget(self.Home)
        self.Accounts = QWidget()
        self.Accounts.setObjectName(u"Accounts")
        self.stackedWidget.addWidget(self.Accounts)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.stackedWidget.addWidget(self.Settings)
        self.Commands = QWidget()
        self.Commands.setObjectName(u"Commands")
        self.stackedWidget.addWidget(self.Commands)
        self.About = QWidget()
        self.About.setObjectName(u"About")
        self.stackedWidget.addWidget(self.About)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 9, 3)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.aboutbtn = QPushButton(self.centralwidget)
        self.aboutbtn.setObjectName(u"aboutbtn")
        self.aboutbtn.setStyleSheet(u"QPushButton {\n"
"	border-radius:9px;\n"
"	padding: 1px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.aboutbtn)

        self.horizontalLayout_3.setStretch(0, 8)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 29)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 14)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        owoDusk.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(owoDusk)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 784, 20))
        owoDusk.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(owoDusk)
        self.statusbar.setObjectName(u"statusbar")
        owoDusk.setStatusBar(self.statusbar)

        self.retranslateUi(owoDusk)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(owoDusk)
    # setupUi

    def retranslateUi(self, owoDusk):
        owoDusk.setWindowTitle(QCoreApplication.translate("owoDusk", u"MainWindow", None))
        self.homebtn.setText(QCoreApplication.translate("owoDusk", u"Home ", None))
        self.accountsbtn.setText(QCoreApplication.translate("owoDusk", u"Accounts ", None))
        self.settingsbtn.setText(QCoreApplication.translate("owoDusk", u"Settings ", None))
        self.commandsbtn.setText(QCoreApplication.translate("owoDusk", u"commands ", None))
        self.logo.setText(QCoreApplication.translate("owoDusk", u"logo", None))
        self.label.setText(QCoreApplication.translate("owoDusk", u"v2.2.0", None))
        self.label_2.setText(QCoreApplication.translate("owoDusk", u"Home", None))
        self.textBrowser.setHtml(QCoreApplication.translate("owoDusk", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#b3f7ff;\">account[1] ran hunt</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#b3f7ff;\">account[1] ran battle</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\">account[2] ran OwO</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#813d9c;\">account[1] prayed &lt;userid&gt;</span></p></body></html>", None))
        self.aboutbtn.setText(QCoreApplication.translate("owoDusk", u"About", None))
    # retranslateUi

