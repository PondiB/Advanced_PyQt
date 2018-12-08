import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

import progress
import sysInfo

class MainUiClass(QtGui.QMainWindow, progress.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUiClass, self).__init__(parent)
        self.setupUi(self)
        self.threadclass = ThreadClass()
        self.threadclass.start()
        self.connect(self.threadclass,QtCore.SIGNAL('CPU_VALUE'),self.updateProgressBar)
 

    def updateProgressBar(self, val):
        val = sysInfo.getCPU()
        self.progressBar.setValue(val)

class ThreadClass(QtCore.QThread):
    def __init__(self,parent = None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        while 1:
            val = sysInfo.getCPU()
            self.emit(QtCore.SIGNAL('CPU_VALUE'), val)

if __name__ == '__main__':
    a = QtGui.QApplication(sys.argv)
    app = MainUiClass()
    app.show()
    a.exec_()
    