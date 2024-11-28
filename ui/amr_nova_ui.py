# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'amr_nova.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1400, 900)
        MainWindow.setStyleSheet(u"\n"
"    QPushButton:hover { background-color: #e0e0e0; }\n"
"    QPushButton:pressed { background-color: #c0c0c0; }\n"
"    QPushButton#emergencyStopButton {\n"
"        color: white;\n"
"        background-color: red;\n"
"        font-weight: bold;\n"
"    }\n"
"            ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainVerticalLayout = QVBoxLayout(self.centralwidget)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        self.statusBarLayout = QHBoxLayout()
        self.statusBarLayout.setSpacing(20)
        self.statusBarLayout.setContentsMargins(10, 10, 10, 10)
        self.statusBarLayout.setObjectName(u"statusBarLayout")
        self.robotStatusLabel = QLabel(self.centralwidget)
        self.robotStatusLabel.setObjectName(u"robotStatusLabel")
        font = QFont()
        font.setPointSize(14)
        self.robotStatusLabel.setFont(font)

        self.statusBarLayout.addWidget(self.robotStatusLabel, 0, Qt.AlignmentFlag.Qt.AlignmentFlag.AlignVCenter)

        self.batteryStatusLabel = QLabel(self.centralwidget)
        self.batteryStatusLabel.setObjectName(u"batteryStatusLabel")
        self.batteryStatusLabel.setFont(font)

        self.statusBarLayout.addWidget(self.batteryStatusLabel, 0, |Qt.AlignmentFlag.AlignVCenter)

        self.velocityStatusLabel = QLabel(self.centralwidget)
        self.velocityStatusLabel.setObjectName(u"velocityStatusLabel")
        self.velocityStatusLabel.setFont(font)

        self.statusBarLayout.addWidget(self.velocityStatusLabel, 0, Qt.AlignmentFlag.Qt.AlignmentFlag.AlignVCenter)


        self.mainVerticalLayout.addLayout(self.statusBarLayout)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.leftControlFrame = QFrame(self.centralwidget)
        self.leftControlFrame.setObjectName(u"leftControlFrame")
        self.leftControlFrame.setMinimumSize(QSize(220, 0))
        self.leftControlFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftControlLayout = QVBoxLayout(self.leftControlFrame)
        self.leftControlLayout.setSpacing(15)
        self.leftControlLayout.setContentsMargins(10, 10, 10, 10)
        self.leftControlLayout.setObjectName(u"leftControlLayout")
        self.mainPageButton = QPushButton(self.leftControlFrame)
        self.mainPageButton.setObjectName(u"mainPageButton")
        self.mainPageButton.setMinimumSize(QSize(200, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.mainPageButton.setFont(font1)

        self.leftControlLayout.addWidget(self.mainPageButton)

        self.connectButton = QPushButton(self.leftControlFrame)
        self.connectButton.setObjectName(u"connectButton")
        self.connectButton.setMinimumSize(QSize(200, 50))
        self.connectButton.setFont(font1)

        self.leftControlLayout.addWidget(self.connectButton)

        self.disconnectButton = QPushButton(self.leftControlFrame)
        self.disconnectButton.setObjectName(u"disconnectButton")
        self.disconnectButton.setMinimumSize(QSize(200, 50))
        self.disconnectButton.setFont(font1)

        self.leftControlLayout.addWidget(self.disconnectButton)

        self.line = QFrame(self.leftControlFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.leftControlLayout.addWidget(self.line)

        self.emergencyStopButton = QPushButton(self.leftControlFrame)
        self.emergencyStopButton.setObjectName(u"emergencyStopButton")
        self.emergencyStopButton.setMinimumSize(QSize(200, 60))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.emergencyStopButton.setFont(font2)

        self.leftControlLayout.addWidget(self.emergencyStopButton)


        self.mainLayout.addWidget(self.leftControlFrame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.mainPageLayout = QVBoxLayout(self.mainPage)
        self.mainPageLayout.setSpacing(20)
        self.mainPageLayout.setContentsMargins(20, 20, 20, 20)
        self.mainPageLayout.setObjectName(u"mainPageLayout")
        self.mainMapFrame = QFrame(self.mainPage)
        self.mainMapFrame.setObjectName(u"mainMapFrame")
        self.mainMapFrame.setFrameShape(QFrame.Shape.Box)
        self.mainMapLayout = QVBoxLayout(self.mainMapFrame)
        self.mainMapLayout.setObjectName(u"mainMapLayout")
        self.mainMapLabel = QLabel(self.mainMapFrame)
        self.mainMapLabel.setObjectName(u"mainMapLabel")
        self.mainMapLabel.setMinimumSize(QSize(0, 500))
        font3 = QFont()
        font3.setPointSize(16)
        self.mainMapLabel.setFont(font3)
        self.mainMapLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainMapLayout.addWidget(self.mainMapLabel)


        self.mainPageLayout.addWidget(self.mainMapFrame)

        self.mainButtonLayout = QHBoxLayout()
        self.mainButtonLayout.setSpacing(50)
        self.mainButtonLayout.setObjectName(u"mainButtonLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.mainButtonLayout.addItem(self.horizontalSpacer)

        self.mappingButtonMain = QPushButton(self.mainPage)
        self.mappingButtonMain.setObjectName(u"mappingButtonMain")
        self.mappingButtonMain.setMinimumSize(QSize(200, 60))
        self.mappingButtonMain.setFont(font)

        self.mainButtonLayout.addWidget(self.mappingButtonMain)

        self.navigationButtonMain = QPushButton(self.mainPage)
        self.navigationButtonMain.setObjectName(u"navigationButtonMain")
        self.navigationButtonMain.setMinimumSize(QSize(200, 60))
        self.navigationButtonMain.setFont(font)

        self.mainButtonLayout.addWidget(self.navigationButtonMain)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.mainButtonLayout.addItem(self.horizontalSpacer_2)


        self.mainPageLayout.addLayout(self.mainButtonLayout)

        self.stackedWidget.addWidget(self.mainPage)
        self.mappingPage = QWidget()
        self.mappingPage.setObjectName(u"mappingPage")
        self.mappingPageLayout = QVBoxLayout(self.mappingPage)
        self.mappingPageLayout.setSpacing(20)
        self.mappingPageLayout.setContentsMargins(20, 20, 20, 20)
        self.mappingPageLayout.setObjectName(u"mappingPageLayout")
        self.mappingMapFrame = QFrame(self.mappingPage)
        self.mappingMapFrame.setObjectName(u"mappingMapFrame")
        self.mappingMapFrame.setFrameShape(QFrame.Shape.Box)
        self.mappingMapLayout = QVBoxLayout(self.mappingMapFrame)
        self.mappingMapLayout.setObjectName(u"mappingMapLayout")
        self.mappingMapLabel = QLabel(self.mappingMapFrame)
        self.mappingMapLabel.setObjectName(u"mappingMapLabel")
        self.mappingMapLabel.setMinimumSize(QSize(0, 500))
        self.mappingMapLabel.setFont(font3)
        self.mappingMapLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mappingMapLayout.addWidget(self.mappingMapLabel)


        self.mappingPageLayout.addWidget(self.mappingMapFrame)

        self.mappingButtonLayout = QGridLayout()
        self.mappingButtonLayout.setSpacing(30)
        self.mappingButtonLayout.setContentsMargins(10, 10, 10, 10)
        self.mappingButtonLayout.setObjectName(u"mappingButtonLayout")
        self.startMappingButton = QPushButton(self.mappingPage)
        self.startMappingButton.setObjectName(u"startMappingButton")
        self.startMappingButton.setMinimumSize(QSize(180, 50))
        self.startMappingButton.setFont(font1)

        self.mappingButtonLayout.addWidget(self.startMappingButton, 0, 0, 1, 1)

        self.saveMapButton = QPushButton(self.mappingPage)
        self.saveMapButton.setObjectName(u"saveMapButton")
        self.saveMapButton.setMinimumSize(QSize(180, 50))
        self.saveMapButton.setFont(font1)

        self.mappingButtonLayout.addWidget(self.saveMapButton, 0, 1, 1, 1)

        self.stopMappingButton = QPushButton(self.mappingPage)
        self.stopMappingButton.setObjectName(u"stopMappingButton")
        self.stopMappingButton.setMinimumSize(QSize(180, 50))
        self.stopMappingButton.setFont(font1)

        self.mappingButtonLayout.addWidget(self.stopMappingButton, 0, 2, 1, 1)

        self.saveWaypointsButton = QPushButton(self.mappingPage)
        self.saveWaypointsButton.setObjectName(u"saveWaypointsButton")
        self.saveWaypointsButton.setMinimumSize(QSize(180, 50))
        self.saveWaypointsButton.setFont(font1)

        self.mappingButtonLayout.addWidget(self.saveWaypointsButton, 1, 0, 1, 1)

        self.saveProhibitionAreasButton = QPushButton(self.mappingPage)
        self.saveProhibitionAreasButton.setObjectName(u"saveProhibitionAreasButton")
        self.saveProhibitionAreasButton.setMinimumSize(QSize(180, 50))
        self.saveProhibitionAreasButton.setFont(font1)

        self.mappingButtonLayout.addWidget(self.saveProhibitionAreasButton, 1, 1, 1, 1)


        self.mappingPageLayout.addLayout(self.mappingButtonLayout)

        self.stackedWidget.addWidget(self.mappingPage)
        self.navigationPage = QWidget()
        self.navigationPage.setObjectName(u"navigationPage")
        self.navigationPageLayout = QVBoxLayout(self.navigationPage)
        self.navigationPageLayout.setSpacing(20)
        self.navigationPageLayout.setContentsMargins(20, 20, 20, 20)
        self.navigationPageLayout.setObjectName(u"navigationPageLayout")
        self.navigationMapFrame = QFrame(self.navigationPage)
        self.navigationMapFrame.setObjectName(u"navigationMapFrame")
        self.navigationMapFrame.setFrameShape(QFrame.Shape.Box)
        self.navigationMapLayout = QVBoxLayout(self.navigationMapFrame)
        self.navigationMapLayout.setObjectName(u"navigationMapLayout")
        self.navigationMapLabel = QLabel(self.navigationMapFrame)
        self.navigationMapLabel.setObjectName(u"navigationMapLabel")
        self.navigationMapLabel.setMinimumSize(QSize(0, 500))
        self.navigationMapLabel.setFont(font3)
        self.navigationMapLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.navigationMapLayout.addWidget(self.navigationMapLabel)


        self.navigationPageLayout.addWidget(self.navigationMapFrame)

        self.navigationButtonLayout = QGridLayout()
        self.navigationButtonLayout.setSpacing(30)
        self.navigationButtonLayout.setContentsMargins(10, 10, 10, 10)
        self.navigationButtonLayout.setObjectName(u"navigationButtonLayout")
        self.startNavigationButton = QPushButton(self.navigationPage)
        self.startNavigationButton.setObjectName(u"startNavigationButton")
        self.startNavigationButton.setMinimumSize(QSize(180, 50))
        self.startNavigationButton.setFont(font1)

        self.navigationButtonLayout.addWidget(self.startNavigationButton, 0, 0, 1, 1)

        self.stopNavigationButton = QPushButton(self.navigationPage)
        self.stopNavigationButton.setObjectName(u"stopNavigationButton")
        self.stopNavigationButton.setMinimumSize(QSize(180, 50))
        self.stopNavigationButton.setFont(font1)

        self.navigationButtonLayout.addWidget(self.stopNavigationButton, 0, 1, 1, 1)

        self.pauseNavigationButton = QPushButton(self.navigationPage)
        self.pauseNavigationButton.setObjectName(u"pauseNavigationButton")
        self.pauseNavigationButton.setMinimumSize(QSize(180, 50))
        self.pauseNavigationButton.setFont(font1)

        self.navigationButtonLayout.addWidget(self.pauseNavigationButton, 0, 2, 1, 1)

        self.resumeNavigationButton = QPushButton(self.navigationPage)
        self.resumeNavigationButton.setObjectName(u"resumeNavigationButton")
        self.resumeNavigationButton.setMinimumSize(QSize(180, 50))
        self.resumeNavigationButton.setFont(font1)

        self.navigationButtonLayout.addWidget(self.resumeNavigationButton, 0, 3, 1, 1)


        self.navigationPageLayout.addLayout(self.navigationButtonLayout)

        self.stackedWidget.addWidget(self.navigationPage)

        self.mainLayout.addWidget(self.stackedWidget)


        self.mainVerticalLayout.addLayout(self.mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AMR Dynamic Layout - Final", None))
        self.robotStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Robot Status: Disconnected", None))
        self.batteryStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Battery: 100%", None))
        self.velocityStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Linear: 0.00 m/s, Angular: 0.00 rad/s", None))
#if QT_CONFIG(tooltip)
        self.mainPageButton.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Main Page", None))
#endif // QT_CONFIG(tooltip)
        self.mainPageButton.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
#if QT_CONFIG(tooltip)
        self.connectButton.setToolTip(QCoreApplication.translate("MainWindow", u"Connect to the robot", None))
#endif // QT_CONFIG(tooltip)
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
#if QT_CONFIG(tooltip)
        self.disconnectButton.setToolTip(QCoreApplication.translate("MainWindow", u"Disconnect from the robot", None))
#endif // QT_CONFIG(tooltip)
        self.disconnectButton.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
#if QT_CONFIG(tooltip)
        self.emergencyStopButton.setToolTip(QCoreApplication.translate("MainWindow", u"Immediately stop the robot", None))
#endif // QT_CONFIG(tooltip)
        self.emergencyStopButton.setText(QCoreApplication.translate("MainWindow", u"Emergency Stop", None))
        self.mainMapLabel.setText(QCoreApplication.translate("MainWindow", u"Main Map View", None))
#if QT_CONFIG(tooltip)
        self.mappingButtonMain.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Mapping page", None))
#endif // QT_CONFIG(tooltip)
        self.mappingButtonMain.setText(QCoreApplication.translate("MainWindow", u"Mapping", None))
#if QT_CONFIG(tooltip)
        self.navigationButtonMain.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Navigation page", None))
#endif // QT_CONFIG(tooltip)
        self.navigationButtonMain.setText(QCoreApplication.translate("MainWindow", u"Navigation", None))
        self.mappingMapLabel.setText(QCoreApplication.translate("MainWindow", u"Mapping Map View", None))
#if QT_CONFIG(tooltip)
        self.startMappingButton.setToolTip(QCoreApplication.translate("MainWindow", u"Begin mapping process", None))
#endif // QT_CONFIG(tooltip)
        self.startMappingButton.setText(QCoreApplication.translate("MainWindow", u"Start Mapping", None))
#if QT_CONFIG(tooltip)
        self.saveMapButton.setToolTip(QCoreApplication.translate("MainWindow", u"Save the current map", None))
#endif // QT_CONFIG(tooltip)
        self.saveMapButton.setText(QCoreApplication.translate("MainWindow", u"Save Map", None))
#if QT_CONFIG(tooltip)
        self.stopMappingButton.setToolTip(QCoreApplication.translate("MainWindow", u"End mapping process", None))
#endif // QT_CONFIG(tooltip)
        self.stopMappingButton.setText(QCoreApplication.translate("MainWindow", u"Stop Mapping", None))
#if QT_CONFIG(tooltip)
        self.saveWaypointsButton.setToolTip(QCoreApplication.translate("MainWindow", u"Save waypoints on the map", None))
#endif // QT_CONFIG(tooltip)
        self.saveWaypointsButton.setText(QCoreApplication.translate("MainWindow", u"Save Waypoints", None))
#if QT_CONFIG(tooltip)
        self.saveProhibitionAreasButton.setToolTip(QCoreApplication.translate("MainWindow", u"Save prohibited areas on the map", None))
#endif // QT_CONFIG(tooltip)
        self.saveProhibitionAreasButton.setText(QCoreApplication.translate("MainWindow", u"Save Prohibition Areas", None))
        self.navigationMapLabel.setText(QCoreApplication.translate("MainWindow", u"Navigation Map View", None))
#if QT_CONFIG(tooltip)
        self.startNavigationButton.setToolTip(QCoreApplication.translate("MainWindow", u"Begin navigation", None))
#endif // QT_CONFIG(tooltip)
        self.startNavigationButton.setText(QCoreApplication.translate("MainWindow", u"Start Navigation", None))
#if QT_CONFIG(tooltip)
        self.stopNavigationButton.setToolTip(QCoreApplication.translate("MainWindow", u"End navigation", None))
#endif // QT_CONFIG(tooltip)
        self.stopNavigationButton.setText(QCoreApplication.translate("MainWindow", u"Stop Navigation", None))
#if QT_CONFIG(tooltip)
        self.pauseNavigationButton.setToolTip(QCoreApplication.translate("MainWindow", u"Pause navigation", None))
#endif // QT_CONFIG(tooltip)
        self.pauseNavigationButton.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
#if QT_CONFIG(tooltip)
        self.resumeNavigationButton.setToolTip(QCoreApplication.translate("MainWindow", u"Resume navigation", None))
#endif // QT_CONFIG(tooltip)
        self.resumeNavigationButton.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
    # retranslateUi

