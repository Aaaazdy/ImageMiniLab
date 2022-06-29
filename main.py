import sys
from lab4 import *
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = ImageMiniLab()
    myWin.show()
    sys.exit(app.exec_())
