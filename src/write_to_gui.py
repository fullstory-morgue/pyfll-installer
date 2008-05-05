# -*- coding: utf-8 -*-

__author__    = 'Horst Tritremmel'
__copyright__ = '(C) 2008 Horst Tritremmel <hjt@sidux.com>'
__license__   = 'GPLv2 or any later version'

from PyQt4 import QtCore, QtGui
from callback import *


TABLEWIDGET_CHECKBOX_NAME = 'tableWidget_checkBox'
FILESYSTEM_LABEL_COLUMN   = 1
FORMAT_WITH_COMBO_COLUMN  = 3
MOUNTPOINT_COMBO_COLUMN   = 4


#
# write to gui
#
class Write_to_gui(object):
    '''
    write values to widgets
    '''
    print 'class Write_to_gui __init__'

    def __init__(self, ui, widgetName):
        self.ui = ui
        self.widgetName = widgetName

        ''' find and set the widget by widgetName '''
        self.widget = self.ui.centralwidget.findChild(QtGui.QWidget, self.widgetName)

        self.checkBox = QtGui.QCheckBox()


    def setHorizontalHeader(self):
        ''' setHorizontalHeader '''

        self.header = \
        [
        QtGui.QApplication.translate("TableEditor", "Partition", None, QtGui.QApplication.UnicodeUTF8),
        QtGui.QApplication.translate("TableEditor", "Filesystem", None, QtGui.QApplication.UnicodeUTF8),
        QtGui.QApplication.translate("TableEditor", "Format", None, QtGui.QApplication.UnicodeUTF8),
        QtGui.QApplication.translate("TableEditor", "Format with", None, QtGui.QApplication.UnicodeUTF8),
        QtGui.QApplication.translate("TableEditor", "Mountpoint", None, QtGui.QApplication.UnicodeUTF8),
        QtGui.QApplication.translate("TableEditor", "UUID", None, QtGui.QApplication.UnicodeUTF8)
        ]

        for self.text in self.header:
            self.headerItem = QtGui.QTableWidgetItem()
            self.headerItem.setText(self.text)
            self.pos = self.header.index(self.text)
            self.widget.setHorizontalHeaderItem(self.pos, self.headerItem)



    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Table
    def cells_to_table(self, row, column):
        ''' add Row and Column to tableWidget '''
        self.widget.clear()
        self.widget.setRowCount(row)
        self.widget.setColumnCount(column)


    # ------------------------------------------------------ Table checkbox
    def checkbox_to_table(self, place):
        ''' add Checkbox to tableWidget '''

        # place[0] at end of name is neccesary for "def table_cb"
        self.checkBox.setObjectName("%s%s" % (TABLEWIDGET_CHECKBOX_NAME, str(place[0])))
        self.tablecb = self.table_cb    # init self.table_cb
        QtCore.QObject.connect(self.checkBox,QtCore.SIGNAL("toggled(bool)"), self.tablecb)

        self.widget.setCellWidget(place[0], place[1], self.checkBox)
        self.labeltext_to_table(place, '')


    def table_cb(self):
        '''
        callback for checkboxes in tableWidget
        hide or show the fromat_with comboBox in tableWidget
        '''

        # get row from checkBox.objectName
        # (the number from end of name: tableWidget_checkBox0, tableWidget_checkBox1, ...)
        self.table_row = int(self.checkBox.objectName().split(TABLEWIDGET_CHECKBOX_NAME)[1])

        # get the comboBox format_with
        self.format_with_combo = self.ui.tableWidget_mountpoints.cellWidget(self.table_row, FORMAT_WITH_COMBO_COLUMN)

        # enable/disable format_with_combo
        if self.checkBox.checkState() == 2:   # if checkBox = on
            print 'enable the format_with comboBox'
            self.format_with_combo.setEnabled(True)
        else:                                 # if checkBox = off
            print 'disable the format_with comboBox'
            self.format_with_combo.setEnabled(False)

        # disable/enable the mountpoint comboBox
        # if filesystemtyp is available
        self.enable_mountpoint_combo(self.table_row)
    # ---------------------------------------------------------------------


    def combobox_to_table(self, place, text):
        ''' add combobox to tableWidget '''

        self.comboBox = QtGui.QComboBox()
        self.comboBox.setObjectName("comboBox_table")
        for t in text:
            self.comboBox.addItem(QtGui.QApplication.translate("", t, None, QtGui.QApplication.UnicodeUTF8))

        # disable the format_with comboBox at start
        if place[1] == FORMAT_WITH_COMBO_COLUMN:
            self.comboBox.setEnabled(False)

        # set the widget to table
        self.widget.setCellWidget(place[0], place[1], self.comboBox)

        # disable the mountpoint comboBox at start
        # if filesystemtyp is available
        if place[1] == MOUNTPOINT_COMBO_COLUMN:
            self.enable_mountpoint_combo(place[0])


    def enable_mountpoint_combo(self, table_row):
        # enable the mountpoint comboBox
        # if filesystemtyp is available
        # or format_checkbox is on
        self.table_row = table_row
        self.mountpoint_combo = self.ui.tableWidget_mountpoints.cellWidget(self.table_row, MOUNTPOINT_COMBO_COLUMN)
        self.fs_label =  self.ui.tableWidget_mountpoints.item(self.table_row, FILESYSTEM_LABEL_COLUMN)

        if len(self.fs_label.text()) == 0 and \
        self.checkBox.checkState() == 0:
            self.mountpoint_combo.setCurrentIndex(0)
            self.mountpoint_combo.setEnabled(False)
        else:
            self.mountpoint_combo.setEnabled(True)


    def labeltext_to_table(self, place, text):
        ''' singleline Text to tableWidget '''
        item = QtGui.QTableWidgetItem(str(text))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.widget.setItem(place[0], place[1], item)


    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    '''
    comboBox
    '''
    def text_to_combobox(self, text):
        ''' add Items to comboBox '''
        for t in text:
            self.widget.addItem(QtGui.QApplication.translate("", t, None, QtGui.QApplication.UnicodeUTF8))


    '''
    singleline Text to lineEdit or label
    '''
    def text_to_singleline(self, text):
        ''' add singleline Text to lineEdit or label '''
        self.widget.setText(QtGui.QApplication.translate("", text, None, QtGui.QApplication.UnicodeUTF8))
