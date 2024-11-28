import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 加载 .ui 文件
        ui_file_name = "amr_nova/ui/nova.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)
        loader = QUiLoader()
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        if not self.ui:
            print(loader.errorString())
            sys.exit(-1)

        # 设置窗口标题
        self.setWindowTitle("AMR Control Panel")

        # 将 UI 元素添加到主窗口
        self.setCentralWidget(self.ui)

        # 连接信号和槽
        self.connect_signals()

    def connect_signals(self):
        # 左侧按钮栏
        self.ui.mainPageButton.clicked.connect(self.show_main_page)
        self.ui.connectButton.clicked.connect(self.connect_to_robot)
        self.ui.disconnectButton.clicked.connect(self.disconnect_from_robot)
        self.ui.emergencyStopButton.clicked.connect(self.emergency_stop)

        # 主页面按钮
        self.ui.mappingButtonMain.clicked.connect(self.show_mapping_page)
        self.ui.navigationButtonMain.clicked.connect(self.show_navigation_page)

        # 建图页面按钮
        self.ui.startMappingButton.clicked.connect(self.start_mapping)
        self.ui.stopMappingButton.clicked.connect(self.stop_mapping)
        self.ui.saveMapButton.clicked.connect(self.save_map)
        self.ui.saveWaypointsButton.clicked.connect(self.save_waypoints)
        self.ui.saveProhibitionAreasButton.clicked.connect(self.save_prohibition_areas)

        # 导航页面按钮
        self.ui.startNavigationButton.clicked.connect(self.start_navigation)
        self.ui.stopNavigationButton.clicked.connect(self.stop_navigation)
        self.ui.pauseNavigationButton.clicked.connect(self.pause_navigation)
        self.ui.resumeNavigationButton.clicked.connect(self.resume_navigation)

    # 页面切换函数
    def show_main_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.mainPage)

    def show_mapping_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.mappingPage)

    def show_navigation_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.navigationPage)

    # 功能实现（占位符）
    def connect_to_robot(self):
        # 在这里添加连接机器人的代码
        QMessageBox.information(self, "Connect", "Connecting to the robot...")
        self.ui.robotStatusLabel.setText("Robot Status: Connected")

    def disconnect_from_robot(self):
        # 在这里添加断开连接的代码
        QMessageBox.information(self, "Disconnect", "Disconnecting from the robot...")
        self.ui.robotStatusLabel.setText("Robot Status: Disconnected")

    def emergency_stop(self):
        # 在这里添加紧急停止的代码
        QMessageBox.warning(self, "Emergency Stop", "Emergency stop activated!")
        # 可能需要更新机器人状态

    def start_mapping(self):
        # 在这里添加开始建图的代码
        QMessageBox.information(self, "Start Mapping", "Mapping started.")

    def stop_mapping(self):
        # 在这里添加停止建图的代码
        QMessageBox.information(self, "Stop Mapping", "Mapping stopped.")

    def save_map(self):
        # 在这里添加保存地图的代码
        QMessageBox.information(self, "Save Map", "Map saved successfully.")

    def save_waypoints(self):
        # 在这里添加保存航点的代码
        QMessageBox.information(self, "Save Waypoints", "Waypoints saved successfully.")

    def save_prohibition_areas(self):
        # 在这里添加保存禁区的代码
        QMessageBox.information(self, "Save Prohibition Areas", "Prohibition areas saved successfully.")

    def start_navigation(self):
        # 在这里添加开始导航的代码
        QMessageBox.information(self, "Start Navigation", "Navigation started.")

    def stop_navigation(self):
        # 在这里添加停止导航的代码
        QMessageBox.information(self, "Stop Navigation", "Navigation stopped.")

    def pause_navigation(self):
        # 在这里添加暂停导航的代码
        QMessageBox.information(self, "Pause Navigation", "Navigation paused.")

    def resume_navigation(self):
        # 在这里添加恢复导航的代码
        QMessageBox.information(self, "Resume Navigation", "Navigation resumed.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())