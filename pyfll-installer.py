# -*- coding: utf-8 -*-

__author__    = 'Horst Tritremmel'
__copyright__ = '(C) 2008 Horst Tritremmel <hjt@sidux.com>'
__license__   = 'GPLv2 or any later version'


import os
import commands
import sys
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


class Error(Exception):
    ''' A generic error handler that does nothing. '''
    pass


class FLLInstaller(object):
    def __init__(self, conf_file):
        self.conf_file = conf_file

        ''' read config file and write values to widgets '''
        self.cfile = ConfigObj(self.conf_file)
        self.tzfile = self.cfile['timezone']['tz_file']

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
        self.file = open(self.tzfile)
        self.tz = self.file.readline()
        self.file.close()

        self.wg = Write_to_gui(self.ui, "label_timezone")
        self.wg.text_to_singleline(r'<span style=" font-size:10pt; font-weight:600;">%s</span>' % (str(self.tz)) )


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
        self.row     = 20
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
                ''' disks comboBox_partition '''

                self.wg = Write_to_gui(self.ui, 'comboBox_partition')
                self.wg.text_to_combobox(self.dev.split())
            else:
                self.fdisk_l = commands.getoutput('fdisk -l %s' % (self.dev)).split('\n')
                if len(self.fdisk_l) < 2:
                    # if partition is extended do noting
                    print self.fdisk_l
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

                ''' 3. column in tableWidget = Format_with '''
                self.place = [ self.place[0], 2]
                self.wg.combobox_to_table(self.place, self.cfile['filesystem']['supported'].split())

                ''' 4. column in tableWidget = checkbox format=0|1 '''
                self.place = [ self.place[0], 3 ]
                self.wg.checkbox_to_table(self.place)

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
        ''' root '''
        self.user_id = commands.getoutput('getent passwd ${USER} | cut -d\: -f3')
        if self.user_id != "0":
            print "Requires root!"
            sys.exit(1)

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
        fll = FLLInstaller(conf_file)
        fll.main()
    except KeyboardInterrupt:
        pass
    except Error:
        sys.exit(1)


