import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout =QVBoxLayout()

        url = QLineEdit()
        save_location = QLineEdit()
        progress = QProgressBar()
        download = QPushButton("Download")

        #placeholder text
        url.setPlaceholderText("URL to Download from")
        save_location.setPlaceholderText("File save location")

        progress.setValue(0)
        progress.setAlignment(Qt.AlignCenter)


        layout.addWidget(url)
        layout.addWidget(save_location)
        layout.addWidget(progress)
        layout.addWidget(download)

        #Important
        self.setLayout(layout)

        #Window Title
        self.setWindowTitle("PyDownloader")
        self.setWindowIcon(QIcon('download_icon.png'))
        self.setFocus()

       
   

app = QApplication(sys.argv)
dialog = Downloader()
dialog.show()
app.exec_()