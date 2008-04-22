# -*- coding: utf-8 -*-

__author__    = 'Horst Tritremmel'
__copyright__ = '(C) 2008 Horst Tritremmel <hjt@sidux.com>'
__license__   = 'GPLv2 or any later version'

from PyQt4 import QtCore, QtGui
import commands

#
# read from gui (callbacks)
#
class Callback(QtGui.QMainWindow):
    def __init__(self, ui):
        ''' handle callbacks '''
        self.ui = ui
        QtGui.QWidget.__init__(self)

        ''' switch stack widget '''
        #QtCore.QObject.connect(self.ui.pushButton_print,QtCore.SIGNAL("clicked()"), self.read)
        QtCore.QObject.connect(self.ui.pushButton_next,QtCore.SIGNAL("clicked()"), self.next)
        QtCore.QObject.connect(self.ui.pushButton_prev,QtCore.SIGNAL("clicked()"), self.prev)
        QtCore.QObject.connect(self.ui.stackedWidget,QtCore.SIGNAL("currentChanged(int)"), self.stack_switched)

        ''' hide the prevButton at start '''
        self.ui.pushButton_prev.hide()

        ''' start partiton tool '''
        QtCore.QObject.connect(self.ui.pushButton_patition,QtCore.SIGNAL("clicked()"), self.run_partition_tool)


    def read(self):
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


    def run_partition_tool(self):
        self.device = self.ui.comboBox_partition.currentText()
        if self.ui.radioButton_gparted.isChecked():
            print 'start %s with gparted' % (self.device)
            self.result = commands.getoutput("gparted %s" % ( self.device))
            print self.result

        if self.ui.radioButton_cfdisk.isChecked():
            print 'start %s with cfdisk' % (self.device)
            self.result = commands.getoutput("x-terminal-emulator -e cfdisk %s" % ( self.device))
            print self.result

        if self.ui.radioButton_fdisk.isChecked():
            print 'start %s with fdisk' % (self.device)
            self.result = commands.getoutput("x-terminal-emulator -e  fdisk %s" % ( self.device))
            print self.result
