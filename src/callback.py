# -*- coding: utf-8 -*-

__author__    = 'Horst Tritremmel'
__copyright__ = '(C) 2008 Horst Tritremmel <hjt@sidux.com>'
__license__   = 'GPLv2 or any later version'

import os
from PyQt4 import QtCore, QtGui
from subprocess import *
#from main import Timezone

#
# read from gui (callbacks)
#
class Callback(QtGui.QMainWindow):
    def __init__(self, ui, timezone):
        ''' handle callbacks '''
        self.ui  = ui
        self.tz  = timezone

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

        ''' start timezone selection '''
        QtCore.QObject.connect(self.ui.pushButton_timezone,QtCore.SIGNAL("clicked()"), self.run_timezone)

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
            self.cmd = ['gparted', self.device]

        if self.ui.radioButton_cfdisk.isChecked():
            print 'start %s with cfdisk' % (self.device)
            self.cmd = ['x-terminal-emulator', '-e', 'cfdisk', self.device]

        if self.ui.radioButton_fdisk.isChecked():
            print 'start %s with fdisk' % (self.device)
            self.cmd = ['x-terminal-emulator', '-e', 'fdisk', self.device]

        self.c = Popen(self.cmd, stdout = PIPE, stderr = STDOUT, close_fds = True)
        print self.c.communicate()[0]
        if not self.c.returncode == 0:
            print 'Error: %s' % ( ' '.join(self.cmd) )


    def run_timezone(self):
        self.i = ''

        ''' libqt-perl installed? '''
        self.cmd = ['dpkg', '--get-selections', 'libqt-perl' ]
        self.c = Popen(self.cmd, stdout = PIPE, stderr = STDOUT, close_fds = True)
        if str(self.c.communicate()[0].split()[1]) == 'install':
            self.i = 'qt'
        if not self.c.returncode == 0:
            print 'Error: %s' % ( ' '.join(self.cmd) )

        ''' libgnome2-perl installed? '''
        self.cmd = ['dpkg', '--get-selections', 'libgnome2-perl' ]
        self.c = Popen(self.cmd, stdout = PIPE, stderr = STDOUT, close_fds = True)
        if str(self.c.communicate()[0].split()[1]) == 'install':
            self.i = 'gtk'
        if not self.c.returncode == 0:
            print 'Error: %s' % ( ' '.join(self.cmd) )


        ''' start tzdata '''
        if self.i == 'qt':
            print 'DEBIAN_FRONTEND=kde dpkg-reconfigure tzdata'
            self.cmd = ['dpkg-reconfigure', 'tzdata']
            self.env = os.environ.copy()
            self.env["DEBIAN_FRONTEND"] = "kde"
        elif self.i == 'gtk':
            print 'DEBIAN_FRONTEND=gnome dpkg-reconfigure tzdata'
            self.cmd = ['dpkg-reconfigure', 'tzdata']
            self.env = os.environ.copy()
            self.env["DEBIAN_FRONTEND"] = "gnome"
        else:
            print 'dpkg-reconfigure tzdata'
            self.cmd = ['x-terminal-emulator', '-e', 'dpkg-reconfigure', 'tzdata']
            self.env = os.environ.copy()

        self.c = Popen(self.cmd, env = self.env, stdout = PIPE, stderr = STDOUT, close_fds = True)
        print self.c.communicate()[0]
        if not self.c.returncode == 0:
            print 'Error: %s' % ( ' '.join(self.cmd) )

        self.tz.label_timezone()
