from distutils.core import setup
import py2exe
import sys
from PyQt4 import QtCore, QtGui
from ui.main import Ui_MainWindow
 
sys.path.append('C:\\Windows\\WinSxS\\x86_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.30729.1_none_e163563597edeada')
includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = []
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll']
 
setup(
    name = "Pondi Calculator",
    version = "1.0",
    author = "Pondi Brian",
    copyright = "Copyright (c) 2018",
    options = {"py2exe": {"compressed": 2, 
                          "optimize": 2,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "bundle_files": 1,
                          "dist_dir": "dist",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         }
              },
    zipfile = None,
    windows=['calculator.py']
)