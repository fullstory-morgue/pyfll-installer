#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__    = 'Horst Tritremmel'
__copyright__ = '(C) 2008 Horst Tritremmel <hjt@sidux.com>'
__license__   = 'GPLv2 or any later version'


import os, sys
from configobj import ConfigObj

from PyQt4 import QtCore, QtGui

# own classes
from src.ui_mainwindow import Ui_MainWindow
from src.translations import *
from src.write_to_gui import *
from src.callback import *
from src.disk import *

# files
conf_file = "pyfll-installer.conf"
tz_file   = "/etc/timezone"


class Error(Exception):
    ''' A generic error handler that does nothing. '''
    pass


class FLLInstaller(object):
    def __init__(self, conf_file, tz_file):
        self.conf_file = conf_file
        self.tz_file   = tz_file

        '''
        set ui
        '''
        self.app = QtGui.QApplication(sys.argv)
        self.MainWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)


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

        '''
        label_timezone
        '''
        self.file = open(self.tz_file)
        self.tz = self.file.readline()
        self.file.close()

        self.wg = Write_to_gui(self.ui, "label_timezone")
        self.wg.text_to_singleline(r'<span style=" font-size:10pt; font-weight:600;">%s</span>' % (str(self.tz)) )


    def read_config(self):
        ''' read config file and write values to widgets '''
        self.cfile = ConfigObj(self.conf_file)

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
        self.row     = 20
        self.column  = 6
        self.place_x = 0
        self.place   = []

        self.wg = Write_to_gui(self.ui, 'tableWidget_mountpoints')
        ''' add Row and Column to table '''
        self.wg.cells_to_table(self.row, self.column)

        self.place = [ -1, 1 ]
        for self.dev in Diskinfo().partitions():
            if Diskinfo().udevinfo(self.dev).get('TYP') == 'disk':
                ''' disks comboBox_partition '''

                self.wg = Write_to_gui(self.ui, 'comboBox_partition')
                self.wg.text_to_combobox(self.dev.split())
            else:
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

                ''' 3. column in tableWidget = name of partition '''
                self.place = [ self.place[0], 2]
                self.wg.combobox_to_table(self.place, [ "ext3", "reiserfs" ])

                ''' 4. column in tableWidget = checkbox format=0|1 '''
                self.place = [ self.place[0], 3 ]
                self.wg.checkbox_to_table(self.place)

                ''' 5. column in tableWidget = partition typ '''
                self.id_fs_uuid = Diskinfo().udevinfo(self.dev).get('ID_FS_UUID')
                self.place = [ self.place[0], 4]
                if self.id_fs_uuid != None:
                    self.wg.labeltext_to_table(self.place, str(self.id_fs_uuid.split()[0]))


    def main(self):
        '''
        start translation
        '''
        self.t  = Gettxt()
        self.ts = Gettxt_gui(self.ui, self.MainWindow, self.app)
        self.ts.gettxt_gui_run()

        '''
        values to ui at start
        '''
        fll.default_text()
        fll.read_config()
        fll.partition_start()

        '''
        callbacks from ui
        '''
        self.cb = Callback(self.ui)

        """
        show MainWindow
        """
        self.MainWindow.show()
        sys.exit(self.app.exec_())


#
# main
#
if __name__ == "__main__":
    try:
        fll = FLLInstaller(conf_file, tz_file)
        fll.main()
    except KeyboardInterrupt:
        pass
    except Error:
        sys.exit(1)


