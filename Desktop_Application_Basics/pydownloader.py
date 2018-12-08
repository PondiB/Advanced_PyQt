import os
import sys
import urllib.request
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout =QVBoxLayout()

        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton("Download")
        browse = QPushButton("Browse")

        #placeholder text
        self.url.setPlaceholderText("URL to Download from")
        self.save_location.setPlaceholderText("File save location")

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignCenter)


        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        #Important
        self.setLayout(layout)

        #Window Title
        self.setWindowTitle("PyDownloader")
        self.setWindowIcon(QIcon('download_icon.png'))
        self.setFocus()

        #Event handlers ---= SIGNALS
        download.clicked.connect(self.download)
        browse.clicked.connect(self.browse_file)

    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Save File As", directory =".",
                                                filter = "All Files (*.*)")
        self.save_location.setText(QDir.toNativeSeparators(save_file))

    def download(self):
        url =self.url.text()
        save_location = self.save_location.text()
            
        #Handling internet fail error
        try:
            urllib.request.urlretrieve(url,save_location,self.report)
        except Exception:
            QMessageBox.warning(self,"Warning","The download failed")

        #Reset to default after download
        QMessageBox.information(self, "Information", "The Download is complete")
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")

    def report (self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar *100 /totalsize
            self.progress.setValue(int(percent))


app = QApplication(sys.argv)
dialog = Downloader()
dialog.show()
app.exec_()