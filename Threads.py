import getpass
import os
import time
import winreg
import sys

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtCore import QThread, pyqtSignal

TEMPPATH = "C:\\Users\\" + getpass.getuser() + "\\AppData\\Local\\Temp\\ActivationWindwosOrOffice.txt"
OFFICEREGPATH = ["SOFTWARE\\Microsoft\\Office\\14.0\\Common\\InstallRoot",
                 "SOFTWARE\\Microsoft\\Office\\15.0\\Common\\InstallRoot",
                 "SOFTWARE\\Microsoft\\Office\\16.0\\Common\\InstallRoot"]


class Threads(QThread):
    AotFinishSignal = pyqtSignal(int)
    AotStepOneSignal = pyqtSignal(int)
    AotStepTwoSignal = pyqtSignal(int)
    AotStepThreeSignal = pyqtSignal(int)
    AotOfficePathError = pyqtSignal(int)

    def __init__(self, number, Path=None):
        super(Threads, self).__init__()
        self.option = number
        self.Path = Path

    def viewRegPath(self):
        for i in OFFICEREGPATH:
            try:
                key = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, i)
                value = winreg.QueryValueEx(key, "Path")[0]
                winreg.CloseKey(key)
                return '"' + value + '"'
            except:
                continue
        return -1;

    def run(self):
        if self.option == 1:
            os.popen("slmgr /dlv")
            self.AotFinishSignal.emit(1)
        elif self.option == 2:
            self.AotStepOneSignal.emit(33)
            time.sleep(1)
            os.popen("slmgr /skms kms.03k.org")
            self.AotStepTwoSignal.emit(33)
            time.sleep(1)
            os.popen("slmgr /ato")
            self.AotStepThreeSignal.emit(33)
            time.sleep(1)
            os.popen("slmgr /dlv")
            time.sleep(1)
            self.AotFinishSignal.emit(1)
        elif self.option == 3:
            Path = self.viewRegPath()
            if Path == -1:
                self.AotOfficePathError.emit(1)
                return
            self.AotStepOneSignal.emit(33)
            time.sleep(1)
            self.AotStepTwoSignal.emit(33)
            tempinfo = "正在激活：\n" + \
                       str(os.popen("cscript " + Path + "ospp.vbs /sethst:kms.03k.org").read()) + "\n" + \
                       str(os.popen("cscript " + Path + "ospp.vbs /act").read()) + "\n" + \
                       "激活完毕！\n" + \
                       "激活信息：\n" + \
                       str(os.popen("cscript " + Path + "ospp.vbs /dstatus").read()) + "\n"
            time.sleep(1)
            self.AotStepThreeSignal.emit(33)
            tempfile = open(TEMPPATH, "w+")
            tempfile.write(tempinfo)
            tempfile.close()
            time.sleep(1)
            self.AotFinishSignal.emit(1)
