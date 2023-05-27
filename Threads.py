import getpass
import os
import time
import winreg
import sys

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtCore import QThread, pyqtSignal

OFFICEREGPATH = ["SOFTWARE\\Microsoft\\Office\\14.0\\Common\\InstallRoot",
                 "SOFTWARE\\Microsoft\\Office\\15.0\\Common\\InstallRoot",
                 "SOFTWARE\\Microsoft\\Office\\16.0\\Common\\InstallRoot"]
SYSTEMPATH = 'C:\\Windows\\System32\\'
MAINEXEC = ['KMSService-x86.exe', 'KMSService-x64.exe']
KMSSERVICE = "kms.03k.org"

class Threads(QThread):
    AotFinishSignal = pyqtSignal(int)
    AotStepOneSignal = pyqtSignal(int)
    AotStepTwoSignal = pyqtSignal(int)
    AotStepThreeSignal = pyqtSignal(int)
    AotOfficePathError = pyqtSignal(int)
    GetUserDirSignal = pyqtSignal()

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
            os.popen("slmgr /skms " + KMSSERVICE)
            self.AotStepTwoSignal.emit(33)
            time.sleep(1)
            os.popen("slmgr /ato")
            self.AotStepThreeSignal.emit(33)
            time.sleep(1)
            os.popen("slmgr /dlv")
            time.sleep(1)
            self.AotFinishSignal.emit(1)
        elif self.option == 3:
            self.TEMPPATH = "C:\\Users\\" + getpass.getuser() + "\\AppData\\Local\\Temp\\ActivationWindwosOrOffice.txt"
            Path = self.viewRegPath()
            if Path == -1:
                self.AotOfficePathError.emit(1)
                return
            self.AotStepOneSignal.emit(33)
            time.sleep(1)
            self.UserDirName = []
            while not os.path.exists("C:\\Users\\" + getpass.getuser()):
                self.GetUserDirSignal.emit()
                time.sleep(10)
                if os.path.exists("C:\\Users\\" + self.UserDirName[0]):
                    self.TEMPPATH = "C:\\Users\\" + self.UserDirName[0] + "\\AppData\\Local\\Temp\\ActivationWindwosOrOffice.txt"
                    break
            self.AotStepTwoSignal.emit(33)
            tempinfo = "正在激活：\n" + \
                       str(os.popen("cscript " + Path + "ospp.vbs /sethst:" + KMSSERVICE).read()) + "\n" + \
                       str(os.popen("cscript " + Path + "ospp.vbs /act").read()) + "\n" + \
                       "激活完毕！\n" + \
                       "激活信息：\n" + \
                       str(os.popen("cscript " + Path + "ospp.vbs /dstatus").read()) + "\n"
            time.sleep(1)
            self.AotStepThreeSignal.emit(33)
            tempfile = open(self.TEMPPATH, "w")
            tempfile.write(tempinfo)
            tempfile.close()
            time.sleep(1)
            self.AotFinishSignal.emit(1)
