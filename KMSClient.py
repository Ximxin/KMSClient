import ctypes
import sys
import os
from PyQt5.QtWidgets import QInputDialog

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from Threads import *
from KMSClient_UI import *


class Change_Ui(Ui_MainWindow):
    TEMPPATH = "C:\\Users\\" + getpass.getuser() + "\\AppData\\Local\\Temp\\ActivationWindwosOrOffice.txt"
    def __init__(self, main):
        self.setupUi(main)
        self.ViewWindows.clicked.connect(self.RunView)
        self.ActivationWindows.clicked.connect(self.RunAcWindows)
        self.ActivationOffice.clicked.connect(self.RunAcOffice)

    def RunView(self):
        self.ViewWindows.setDisabled(True)
        QMessageBox.information(self.centralwidget, "提示信息", "正在查询，请稍后...")
        self.ViewThead = Threads(1)
        self.ViewThead.AotFinishSignal.connect(self.ViewWindowsTips)
        self.ViewThead.start()

    def RunAcWindows(self):
        self.ActivationWindows.setDisabled(True)
        self.AcWindowsThread = Threads(2)
        self.AcWindowsThread.AotStepOneSignal.connect(self.OneWindowsBar)
        self.AcWindowsThread.AotStepTwoSignal.connect(self.TwoWindowsBar)
        self.AcWindowsThread.AotStepThreeSignal.connect(self.ThreeWindowsBar)
        self.AcWindowsThread.AotFinishSignal.connect(self.AcWindowsTips)
        self.AcWindowsThread.start()

    def RunAcOffice(self):
        self.ActivationOffice.setDisabled(True)
        self.AcOfficeThread = Threads(3)
        self.AcOfficeThread.AotOfficePathError.connect(self.PathError)
        self.AcOfficeThread.AotStepOneSignal.connect(self.OneOfficeBar)
        self.AcOfficeThread.AotStepTwoSignal.connect(self.TwoOfficeBar)
        self.AcOfficeThread.AotStepThreeSignal.connect(self.ThreeOfficeBar)
        self.AcOfficeThread.AotFinishSignal.connect(self.AcOfficeTips)
        self.AcOfficeThread.GetUserDirSignal.connect(self.GetUserDir)
        self.AcOfficeThread.start()

    def GetUserDir(self):
        self.AcOfficeThread.UserDirName = QInputDialog.getText(self.centralwidget, "获取用户文件夹","请输入用户文件夹名称，"
        "用户文件夹在C:\\Users文件夹下，请查看后填写当前用户的用户文件夹（你只有10秒钟时间，10秒后将刷新此页面）：")
        self.TEMPPATH = "C:\\Users\\" + self.AcOfficeThread.UserDirName[0] + "\\AppData\\Local\\Temp\\ActivationWindwosOrOffice.txt"

    def PathError(self):
        self.AotInfo.setText("未找到你的Office安装路径！请检查是否已安装Office，软件暂不支持32位版本Office！")
        return

    def OneOfficeBar(self):
        self.AotStateBar.setValue(33)
        self.AotInfo.setText("正在初始化...")

    def TwoOfficeBar(self):
        self.AotStateBar.setValue(66)
        self.AotInfo.setText("正在激活...")

    def ThreeOfficeBar(self):
        self.AotStateBar.setValue(100)
        self.AotInfo.setText("正在收集激活信息...")

    def OneWindowsBar(self):
        self.AotStateBar.setValue(33)
        self.AotInfo.setText("正在激活...")

    def TwoWindowsBar(self):
        self.AotStateBar.setValue(66)

    def ThreeWindowsBar(self):
        self.AotStateBar.setValue(100)

    def ViewWindowsTips(self):
        self.ViewWindows.setDisabled(False)
        QMessageBox.information(self.centralwidget, "提示信息", "查询完成，请查看结果！")

    def AcWindowsTips(self):
        self.ActivationWindows.setDisabled(False)
        self.AotInfo.setText("激活完成...")

    def AcOfficeTips(self):
        self.ActivationOffice.setDisabled(False)
        tempfile = open(self.TEMPPATH, "r")
        tempinfo = tempfile.read()
        tempfile.close()
        os.remove(self.TEMPPATH)
        self.ActivationState.setText(tempinfo)
        self.AotInfo.setText("激活完毕,请查看激活信息...")


def is_Admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if __name__ == "__main__":
    if is_Admin():
        app = QApplication(sys.argv)
        Main = QMainWindow()
        Ui = Change_Ui(Main)
        Main.setWindowTitle("Windows激活程序")
        Main.setFixedSize(452, 596)
        Main.setWindowIcon(QIcon("images/favicon.ico"))
        Main.show()
        sys.exit(app.exec_())
    else:
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable, __file__, None, 1)
