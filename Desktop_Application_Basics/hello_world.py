import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class HelloWorld(QDialog):
    def __init__(self):
        #super(HelloWorld, self).__init__(parent)
        QDialog.__init__(self)

        layout =QGridLayout()


        self.label = QLabel("Hello World")
        line_edit = QLineEdit()
        button = QPushButton("Close")


        layout.addWidget(self.label,0,0)
        layout.addWidget(line_edit,0,1)
        layout.addWidget(button,1,1)

        #Important
        self.setLayout(layout)

        button.clicked.connect(self.close)
        line_edit.textChanged.connect(self.changeTextLabel)
        #Old style
        #self.connect(line_edit,SIGNAL("textChanged(QString)"). self.changeTextLabel)

    def changeTextLabel(self, text):
        self.label.setText(text)

app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()