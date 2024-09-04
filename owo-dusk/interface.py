# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTextBrowser, QVBoxLayout, QWidget)

class Ui_owoDusk(object):
    def setupUi(self, owoDusk):
        if not owoDusk.objectName():
            owoDusk.setObjectName(u"owoDusk")
        owoDusk.resize(790, 585)
        owoDusk.setWindowOpacity(1.000000000000000)
        owoDusk.setStyleSheet(u"QMainWindow {\n"
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
"\n"
"")
        self.centralWidget = QWidget(owoDusk)
        self.centralWidget.setObjectName(u"centralWidget")
        self.accountFrame = QFrame(self.centralWidget)
        self.accountFrame.setObjectName(u"accountFrame")
        self.accountFrame.setGeometry(QRect(10, 10, 771, 61))
        self.accountFrame.setStyleSheet(u"")
        self.accountFrame.setFrameShape(QFrame.StyledPanel)
        self.accountFrame.setFrameShadow(QFrame.Raised)
        self.homebtn = QPushButton(self.accountFrame)
        self.homebtn.setObjectName(u"homebtn")
        self.homebtn.setGeometry(QRect(50, 10, 131, 41))
        self.accountsbtn = QPushButton(self.accountFrame)
        self.accountsbtn.setObjectName(u"accountsbtn")
        self.accountsbtn.setGeometry(QRect(230, 10, 131, 41))
        self.settingsbtn = QPushButton(self.accountFrame)
        self.settingsbtn.setObjectName(u"settingsbtn")
        self.settingsbtn.setGeometry(QRect(410, 10, 131, 41))
        self.commandsbtn = QPushButton(self.accountFrame)
        self.commandsbtn.setObjectName(u"commandsbtn")
        self.commandsbtn.setEnabled(True)
        self.commandsbtn.setGeometry(QRect(590, 10, 131, 41))
        self.stackedWidget = QStackedWidget(self.centralWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(70, 90, 711, 451))
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"    background-color: #07000d;\n"
"    border: 0.8px solid #580399;\n"
"	color: #ff87ff;\n"
"	border-radius: 20px;\n"
"}\n"
"QWidget {\n"
"    background-color: #07000d;\n"
"	color: #ff87ff;\n"
"	border-radius: 20px;\n"
"}\n"
"QLabel {\n"
"    background-color: #07000d;\n"
"	color: #ff87ff;\n"
"	font-size: 20px;\n"
"	border: 0;\n"
"}")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.label_2 = QLabel(self.Home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 10, 91, 41))
        self.label_2.setStyleSheet(u"")
        self.console = QTextBrowser(self.Home)
        self.console.setObjectName(u"console")
        self.console.setGeometry(QRect(50, 60, 621, 341))
        self.console.setStyleSheet(u"QTextBrowser {border: none; border-radius: 0px;}")
        self.stackedWidget.addWidget(self.Home)
        self.Accounts = QWidget()
        self.Accounts.setObjectName(u"Accounts")
        self.label = QLabel(self.Accounts)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 10, 91, 41))
        self.stackedWidget.addWidget(self.Accounts)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.label_3 = QLabel(self.Settings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 10, 81, 41))
        self.verticalLayoutWidget = QWidget(self.Settings)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(80, 120, 160, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.verticalLayoutWidget_2 = QWidget(self.Settings)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(440, 120, 160, 201))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_5 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_2.addWidget(self.checkBox_5)

        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.checkBox_6 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_2.addWidget(self.checkBox_6)

        self.stackedWidget.addWidget(self.Settings)
        self.Commands = QWidget()
        self.Commands.setObjectName(u"Commands")
        self.label_4 = QLabel(self.Commands)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 10, 111, 41))
        self.comboBox = QComboBox(self.Commands)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 20, 111, 23))
        self.stackedWidget.addWidget(self.Commands)
        self.About = QWidget()
        self.About.setObjectName(u"About")
        self.About.setStyleSheet(u"QTextBrowser a {\n"
"    color: #d437ce;\n"
"}\n"
"QTextBrowser a:hover {\n"
"    color: #ff00ff;\n"
"}\n"
"")
        self.label_5 = QLabel(self.About)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(260, 20, 161, 51))
        self.textBrowser = QTextBrowser(self.About)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(200, 150, 291, 191))
        self.textBrowser.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.About)
        self.frame = QFrame(self.centralWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 79, 51, 491))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.version_lable = QLabel(self.frame)
        self.version_lable.setObjectName(u"version_lable")
        self.version_lable.setGeometry(QRect(0, 470, 51, 21))
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(10, 10, 31, 31))
        self.aboutbtn = QPushButton(self.centralWidget)
        self.aboutbtn.setObjectName(u"aboutbtn")
        self.aboutbtn.setGeometry(QRect(690, 550, 80, 23))
        owoDusk.setCentralWidget(self.centralWidget)

        self.retranslateUi(owoDusk)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(owoDusk)
    # setupUi

    def retranslateUi(self, owoDusk):
        owoDusk.setWindowTitle(QCoreApplication.translate("owoDusk", u"OwO Dusk", None))
        self.homebtn.setText(QCoreApplication.translate("owoDusk", u"Home", None))
        self.accountsbtn.setText(QCoreApplication.translate("owoDusk", u"Accounts", None))
        self.settingsbtn.setText(QCoreApplication.translate("owoDusk", u"Settings", None))
        self.commandsbtn.setText(QCoreApplication.translate("owoDusk", u"Commands", None))
        self.label_2.setText(QCoreApplication.translate("owoDusk", u"Home", None))
        self.label.setText(QCoreApplication.translate("owoDusk", u" Accounts", None))
        self.label_3.setText(QCoreApplication.translate("owoDusk", u"Settings", None))
        self.checkBox_2.setText(QCoreApplication.translate("owoDusk", u"Offline mode", None))
        self.checkBox.setText(QCoreApplication.translate("owoDusk", u"Use Shortforms", None))
        self.checkBox_3.setText(QCoreApplication.translate("owoDusk", u"Quests Automation", None))
        self.checkBox_5.setText(QCoreApplication.translate("owoDusk", u"Typing Indicator", None))
        self.checkBox_4.setText(QCoreApplication.translate("owoDusk", u"Notifications", None))
        self.checkBox_6.setText(QCoreApplication.translate("owoDusk", u"CheckBox", None))
        self.label_4.setText(QCoreApplication.translate("owoDusk", u"Commands", None))
        self.label_5.setText(QCoreApplication.translate("owoDusk", u"About OwO-Dusk", None))
        self.textBrowser.setHtml(QCoreApplication.translate("owoDusk", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">OwO-dusk</span>,</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The best selfbot currently available for OwO bot.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-i"
                        "ndent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This project was made by EchoQuill and is completely open source!</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Thankyou for your trust in us :&gt;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Links:-</span></p>\n"
"<p style=\""
                        "-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">https://github.com/EchoQuill/owo-dusk</p></body></html>", None))
        self.version_lable.setText(QCoreApplication.translate("owoDusk", u"v2.0.0", None))
        self.logo.setText(QCoreApplication.translate("owoDusk", u"Logo", None))
        self.aboutbtn.setText(QCoreApplication.translate("owoDusk", u"About", None))
    # retranslateUi

