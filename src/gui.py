'''
Created on Oct 7, 2010

@author: Kyle
'''
import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('Ppwn Control Center')
widget.show()

sys.exit(app.exec_())
