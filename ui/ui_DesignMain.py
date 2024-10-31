# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DesignMainjUcvVR.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(481, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.Header = QVBoxLayout()
        self.Header.setSpacing(0)
        self.Header.setObjectName(u"Header")
        self.LHeader = QLabel(self.centralwidget)
        self.LHeader.setObjectName(u"LHeader")
        font = QFont()
        font.setPointSize(28)
        self.LHeader.setFont(font)
        self.LHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Header.addWidget(self.LHeader)


        self.horizontalLayout.addLayout(self.Header)

        self.VLInfo = QVBoxLayout()
        self.VLInfo.setSpacing(0)
        self.VLInfo.setObjectName(u"VLInfo")
        self.LVersion = QLabel(self.centralwidget)
        self.LVersion.setObjectName(u"LVersion")
        font1 = QFont()
        font1.setPointSize(10)
        self.LVersion.setFont(font1)
        self.LVersion.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.LVersion.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.VLInfo.addWidget(self.LVersion)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.VLInfo.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.VLInfo)

        self.horizontalLayout.setStretch(0, 20)
        self.horizontalLayout.setStretch(1, 80)
        self.horizontalLayout.setStretch(2, 20)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.HLContentCenter = QHBoxLayout()
        self.HLContentCenter.setSpacing(0)
        self.HLContentCenter.setObjectName(u"HLContentCenter")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.VLPlaceAttributesSet = QVBoxLayout()
        self.VLPlaceAttributesSet.setObjectName(u"VLPlaceAttributesSet")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.VLPlaceAttributesSet.addWidget(self.label)

        self.VLAttrIn = QVBoxLayout()
        self.VLAttrIn.setObjectName(u"VLAttrIn")
        self.VLAttrInContent = QVBoxLayout()
        self.VLAttrInContent.setObjectName(u"VLAttrInContent")

        self.VLAttrIn.addLayout(self.VLAttrInContent)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.VLAttrIn.addItem(self.verticalSpacer)


        self.VLPlaceAttributesSet.addLayout(self.VLAttrIn)

        self.VLPlaceAttributesSet.setStretch(0, 10)
        self.VLPlaceAttributesSet.setStretch(1, 80)

        self.horizontalLayout_9.addLayout(self.VLPlaceAttributesSet)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.VLPlaceAttributesOut = QVBoxLayout()
        self.VLPlaceAttributesOut.setObjectName(u"VLPlaceAttributesOut")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.VLPlaceAttributesOut.addWidget(self.label_2)

        self.VLAttrOut = QVBoxLayout()
        self.VLAttrOut.setObjectName(u"VLAttrOut")
        self.VLAttrOutContent = QVBoxLayout()
        self.VLAttrOutContent.setObjectName(u"VLAttrOutContent")

        self.VLAttrOut.addLayout(self.VLAttrOutContent)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.VLAttrOut.addItem(self.verticalSpacer_4)


        self.VLPlaceAttributesOut.addLayout(self.VLAttrOut)

        self.VLPlaceAttributesOut.setStretch(0, 10)
        self.VLPlaceAttributesOut.setStretch(1, 80)

        self.horizontalLayout_9.addLayout(self.VLPlaceAttributesOut)

        self.horizontalLayout_9.setStretch(0, 50)
        self.horizontalLayout_9.setStretch(2, 50)

        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PBConsoleVisibDescide = QPushButton(self.centralwidget)
        self.PBConsoleVisibDescide.setObjectName(u"PBConsoleVisibDescide")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBConsoleVisibDescide.sizePolicy().hasHeightForWidth())
        self.PBConsoleVisibDescide.setSizePolicy(sizePolicy)
        self.PBConsoleVisibDescide.setMinimumSize(QSize(100, 30))
        self.PBConsoleVisibDescide.setMaximumSize(QSize(100, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.PBConsoleVisibDescide.setFont(font2)

        self.horizontalLayout_2.addWidget(self.PBConsoleVisibDescide)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.VLConsoleOut = QVBoxLayout()
        self.VLConsoleOut.setObjectName(u"VLConsoleOut")
        self.TEConsoleOutExample = QTextEdit(self.centralwidget)
        self.TEConsoleOutExample.setObjectName(u"TEConsoleOutExample")
        self.TEConsoleOutExample.setReadOnly(True)

        self.VLConsoleOut.addWidget(self.TEConsoleOutExample)


        self.verticalLayout_4.addLayout(self.VLConsoleOut)

        self.verticalLayout_4.setStretch(0, 50)
        self.verticalLayout_4.setStretch(1, 5)
        self.verticalLayout_4.setStretch(2, 50)

        self.HLContentCenter.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addLayout(self.HLContentCenter)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.PBClear = QPushButton(self.centralwidget)
        self.PBClear.setObjectName(u"PBClear")

        self.horizontalLayout_5.addWidget(self.PBClear)

        self.PBCalculate = QPushButton(self.centralwidget)
        self.PBCalculate.setObjectName(u"PBCalculate")

        self.horizontalLayout_5.addWidget(self.PBCalculate)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 80)
        self.verticalLayout_2.setStretch(2, 5)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.LAuthors = QLabel(self.centralwidget)
        self.LAuthors.setObjectName(u"LAuthors")
        self.LAuthors.setFont(font1)
        self.LAuthors.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.LAuthors)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 80)
        self.verticalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LHeader.setText(QCoreApplication.translate("MainWindow", u"AlgoCalc", None))
        self.LVersion.setText(QCoreApplication.translate("MainWindow", u"Version 1.0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.PBConsoleVisibDescide.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u0437\u0432\u0435\u0440\u043d\u0443\u0442\u044c", None))
        self.TEConsoleOutExample.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Fira Code Medium'; font-size:14pt; font-weight:500; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sd,nw bddgf</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sfdg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sfdg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px;\">sf</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">g</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sfdg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sdf</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sdf</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sdf</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-ri"
                        "ght:0px; -qt-block-indent:0; text-indent:0px;\">sdf</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sdf</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sdf</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sdff</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sgd</p></body></html>", None))
        self.PBClear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.PBCalculate.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.LAuthors.setText(QCoreApplication.translate("MainWindow", u"Authors: Yachoy Hedgies, MSA", None))
    # retranslateUi

