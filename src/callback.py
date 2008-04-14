# -*- coding: utf-8 -*-

__author__    = 'Horst Tritremmel'
__copyright__ = '(C) 2008 Horst Tritremmel <hjt@sidux.com>'
__license__   = 'GPLv2 or any later version'

from PyQt4 import QtCore, QtGui

#
# read from gui (callbacks)
#
class Callback(QtGui.QMainWindow):
    def __init__(self, ui):
        self.ui = ui
        QtGui.QWidget.__init__(self)
        #QtCore.QObject.connect(self.ui.pushButton_print,QtCore.SIGNAL("clicked()"), self.read)
        QtCore.QObject.connect(self.ui.pushButton_next,QtCore.SIGNAL("clicked()"), self.next)
        QtCore.QObject.connect(self.ui.pushButton_prev,QtCore.SIGNAL("clicked()"), self.prev)
        QtCore.QObject.connect(self.ui.stackedWidget,QtCore.SIGNAL("currentChanged(int)"), self.stack_switched)
        ''' hide the prevButton at start '''
        self.ui.pushButton_prev.hide()

    def read(self):
        print "\ncomboBox_root: " + self.ui.comboBox_root.currentText()
        print "comboBox_bootloader: " + self.ui.comboBox_bootloader.currentText()

        w = self.ui.tableWidget1.cellWidget(0, 1)
        print "cell (0, 1) from table1: " + w.currentText()

    def next(self):
        self.ui.stackedWidget.setCurrentIndex(int(self.ui.stackedWidget.currentIndex()) + 1)

    def prev(self):
        self.ui.stackedWidget.setCurrentIndex(int(self.ui.stackedWidget.currentIndex()) - 1)

    def stack_switched(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            ''' first tab from stackWidget '''
            self.ui.pushButton_prev.hide()
        else:
            self.ui.pushButton_prev.show()

        if self.ui.stackedWidget.currentIndex() == self.ui.stackedWidget.count() - 1:
            ''' last tab from stackWidget '''
            self.ui.pushButton_next.hide()
        else:
            self.ui.pushButton_next.show()
