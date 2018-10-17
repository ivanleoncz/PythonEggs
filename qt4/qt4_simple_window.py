
import sys
from PyQt4.QtGui import *

a = QApplication(sys.argv)

w = QWidget()
w.resize(320, 240)
w.setWindowTitle("Hello World")

btn = QPushButton("Click Here", w)
btn.setToolTip("Click to quit!")
btn.clicked.connect(exit)
btn.resize(btn.sizeHint())
btn.move(100, 80)

w.show()

sys.exit(a.exec_())
