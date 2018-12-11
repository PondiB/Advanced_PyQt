import PyQt4.QtCore as qc
import PyQt4.QtGui as qg

dialog = None
#---------------------------------------------------------------------#
class NameIt(qg.QDialog):
    def __init__(self):
        qg.QDialog.__init__(self)
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setWindowTitle('Name It')
        self.setFixedHeight(285)
        self.setFixedWidth(320)

        self.setLayout(qg.QVBoxLayout())
        self.layout().setContentsMargins(5,5,5,5)
        self.layout().setSpacing(0)
        self.layout().setAlignment(qc.Qt.AlignTop)

#---------------------------------------------------------------------#
def create():
    global dialog
    if dialog is None:
        dialog = NameIt()
    dialog.show()

def delete():
    global dialog
    if dialog is None:
        return

    dialog.deleteLater()
    dialog =None