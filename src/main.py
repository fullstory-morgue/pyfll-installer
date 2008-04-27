# -*- coding: utf-8 -*-

__author__    = 'Horst Tritremmel'
__copyright__ = '(C) 2008 Horst Tritremmel <hjt@sidux.com>'
__license__   = 'GPLv2 or any later version'

import os
import sys
from subprocess import *



from configobj import ConfigObj
from PyQt4 import QtCore, QtGui

# own classes
from ui_mainwindow import Ui_MainWindow
from translations import *
from write_to_gui import *
from callback import *
from disk import *



class FLLInstaller(object):
    def __init__(self, CONF_FILE):
        self.CONF_FILE = CONF_FILE

        ''' read config file and write values to widgets '''
        self.cfile = ConfigObj(self.CONF_FILE)


    def default_text(self):
        '''
        default text to label widgets.
        you can find the text in src/translations.py
        '''

        '''
        label_start
        '''
        self.wg = Write_to_gui(self.ui, "label_start")
        self.wg.text_to_singleline(str(self.t.label_start()))


    def read_config(self):

        '''
        comboBox
        '''
        for self.c in self.cfile['text_to_comboBox']:
            ''' name in config file must be the same in ui file '''
            self.objectName = self.c[:]
            self.objectValue = self.cfile['text_to_comboBox'][self.objectName]

            self.wg = Write_to_gui(self.ui, self.objectName)
            self.wg.text_to_combobox(self.objectValue.split())

        '''
        lineEdit
        '''
        for self.c in self.cfile['text_to_lineEdit']:
            ''' name in config file must be the same in ui file '''
            self.objectName = self.c[:]
            self.objectValue = self.cfile['text_to_lineEdit'][self.objectName]

            self.wg = Write_to_gui(self.ui, self.objectName)
            self.wg.text_to_singleline(self.objectValue)


    def partition_start(self):
        '''
        comboBox_partition and tableWidget_mountpoints
        '''
        self.row     = Diskinfo().partition_count()
        self.column  = 6
        self.place_x = 0
        self.place   = []
        self.mp      = []

        self.wg = Write_to_gui(self.ui, 'tableWidget_mountpoints')
        ''' add Row and Column to table '''
        self.wg.cells_to_table(self.row, self.column)

        ''' setHorizontalHeader in tableWidget'''
        self.wg.setHorizontalHeader()

        self.place = [ -1, 1 ]
        for self.dev in Diskinfo().partitions():
            if Diskinfo().udevinfo(self.dev).get('TYP') == 'disk':
                '''
                disks ( /dev/sda1, /dev/sda2, ...)
                '''

                ''' comboBox_partition (gparted, fdisk, cfdisk start) '''
                self.wg = Write_to_gui(self.ui, 'comboBox_partition')
                self.wg.text_to_combobox(self.dev.split())

                ''' comboBox_installtarget ( mbr, partition, /dev/sda, ...
                [wihtout usb partitions] '''
                if Diskinfo().udevinfo(self.dev).get('ID_BUS') != "usb":
                    self.wg = Write_to_gui(self.ui, 'comboBox_installtarget')
                    self.wg.text_to_combobox(self.dev.split())

            else:
                '''
                partitions ( /dev/sda1, /dev/sda2, ...)
                '''
                ''' fdisk -l '''
                self.cmd = ['fdisk', '-l', self.dev]

                self.c = Popen(self.cmd, stdout = PIPE, stderr = STDOUT, close_fds = True)
                self.fdisk_l = self.c.communicate()[0]
                if not self.c.returncode == 0:
                    print 'Error: %s' % ( ' '.join(self.cmd) )

                ''' if fdisk -l empty, goto next '''
                if len(self.fdisk_l) < 2:
                    # if partition is extended do noting
                    continue


                ''' partitions to table tableWidget_mountpoints '''
                self.wg = Write_to_gui(self.ui, 'tableWidget_mountpoints')

                ''' 1. column in tableWidget = name of partition '''
                self.place = [ self.place[0] + 1, 0]
                self.wg.labeltext_to_table(self.place, str(self.dev.split()[0]))

                ''' 2. column in tableWidget = partition typ '''
                self.id_fs_type = Diskinfo().udevinfo(self.dev).get('ID_FS_TYPE')
                self.place = [ self.place[0], 1]
                if self.id_fs_type != None:
                    self.wg.labeltext_to_table(self.place, str(self.id_fs_type.split()[0]))
                else:
                    self.wg.labeltext_to_table(self.place, "")

                ''' 3. column in tableWidget = checkbox format=0|1 '''
                self.place = [ self.place[0], 2 ]
                self.wg.checkbox_to_table(self.place)

                ''' 4. column in tableWidget = Format_with '''
                self.place = [ self.place[0], 3]
                self.wg.combobox_to_table(self.place, self.cfile['filesystem']['supported'].split())

                ''' 5. column in tableWidget = mountpoint '''
                self.place = [ self.place[0], 4]
                self.mp = [ "" ]
                self.mp += self.cfile['filesystem']['mountpoints'].split()
                self.wg.combobox_to_table(self.place, self.mp)

                ''' 6. column in tableWidget = partition typ '''
                self.id_fs_uuid = Diskinfo().udevinfo(self.dev).get('ID_FS_UUID')
                self.place = [ self.place[0], 5]
                if self.id_fs_uuid != None:
                    self.wg.labeltext_to_table(self.place, str(self.id_fs_uuid.split()[0]))
                else:
                    self.wg.labeltext_to_table(self.place, "")


    def main(self):
        '''
        set ui
        '''
        self.app = QtGui.QApplication(sys.argv)
        self.MainWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)


        '''
        start translation
        '''
        self.t  = Gettxt()
        self.ts = Gettxt_gui(self.ui, self.MainWindow, self.app)
        self.ts.gettxt_gui_run()


        '''
        values to ui at start
        '''
        self.default_text()
        self.read_config()
        self.partition_start()

        '''
        Timezone to label
        '''
        self.timezone = Timezone(self.ui, self.CONF_FILE)
        self.timezone.label_timezone()

        '''
        callbacks from ui
        '''
        self.cb = Callback(self.ui, self.timezone)

        """
        show MainWindow
        """
        self.MainWindow.show()
        sys.exit(self.app.exec_())


class Timezone(object):
    ''' Timezone class.'''
    def __init__(self, ui, CONFFILE):
        self.ui = ui
        self.CONFFILE = CONFFILE

        ''' read config file and write values to widgets '''
        self.conf = ConfigObj(self.CONFFILE)
        self.tzfile = self.conf['timezone']['tz_file']

    def label_timezone(self):
        pass
        '''
        label_timezone
        '''
        self.file = open(self.tzfile)
        self.tz = self.file.readline()
        self.file.close()

        self.wg = Write_to_gui(self.ui, "label_timezone")
        self.wg.text_to_singleline(r'<span style=" font-size:10pt; font-weight:600;">%s</span>' % (str(self.tz)) )
