# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 981, 451))
        self.tab_base_monitor = QWidget()
        self.tab_base_monitor.setObjectName(u"tab_base_monitor")
        self.tabWidget.addTab(self.tab_base_monitor, "")
        self.tab_rviz = QWidget()
        self.tab_rviz.setObjectName(u"tab_rviz")
        self.tabWidget.addTab(self.tab_rviz, "")
        self.tab_camera = QWidget()
        self.tab_camera.setObjectName(u"tab_camera")
        self.tabWidget.addTab(self.tab_camera, "")
        self.tab_terminal = QWidget()
        self.tab_terminal.setObjectName(u"tab_terminal")
        self.tabWidget.addTab(self.tab_terminal, "")
        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 460, 981, 221))
        self.tab_base_control = QWidget()
        self.tab_base_control.setObjectName(u"tab_base_control")
        self.tabWidget_2.addTab(self.tab_base_control, "")
        self.tab_mapping = QWidget()
        self.tab_mapping.setObjectName(u"tab_mapping")
        self.pushButton = QPushButton(self.tab_mapping)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 30, 101, 23))
        self.pushButton_2 = QPushButton(self.tab_mapping)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 40, 91, 23))
        self.pushButton_5 = QPushButton(self.tab_mapping)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(140, 40, 75, 23))
        self.tabWidget_2.addTab(self.tab_mapping, "")
        self.tab_navigation = QWidget()
        self.tab_navigation.setObjectName(u"tab_navigation")
        self.pushButton_3 = QPushButton(self.tab_navigation)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 40, 75, 23))
        self.pushButton_4 = QPushButton(self.tab_navigation)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(160, 30, 75, 23))
        self.tabWidget_2.addTab(self.tab_navigation, "")
        self.tab_rviz_control = QWidget()
        self.tab_rviz_control.setObjectName(u"tab_rviz_control")
        self.tabWidget_2.addTab(self.tab_rviz_control, "")
        self.tab_command = QWidget()
        self.tab_command.setObjectName(u"tab_command")
        self.tabWidget_2.addTab(self.tab_command, "")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(890, 700, 52, 14))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_base_monitor), QCoreApplication.translate("MainWindow", u"Base Monitor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rviz), QCoreApplication.translate("MainWindow", u"RViz", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_camera), QCoreApplication.translate("MainWindow", u"Camera", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_terminal), QCoreApplication.translate("MainWindow", u"Terminal", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_base_control), QCoreApplication.translate("MainWindow", u"Base Control", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start mapping", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Stop mapping", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Save map", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_mapping), QCoreApplication.translate("MainWindow", u"Mapping", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5bfc\u822a", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u5bfc\u822a", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_navigation), QCoreApplication.translate("MainWindow", u"Navigation", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_rviz_control), QCoreApplication.translate("MainWindow", u"RViz Control", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_command), QCoreApplication.translate("MainWindow", u"Command", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

