# -*- coding: utf-8 -*-

__author__    = 'Horst Tritremmel'
__copyright__ = '(C) 2008 Horst Tritremmel <hjt@sidux.com>'
__license__   = 'GPLv2 or any later version'

from PyQt4 import QtCore, QtGui


#
# write to gui
#
class Write_to_gui(object):
    '''
    write values to widgets
    '''
    def __init__(self, ui, widgetName):
        self.ui = ui
        self.widgetName = widgetName

        ''' find and set the widget by widgetName '''
        self.widget = self.ui.centralwidget.findChild(QtGui.QWidget, self.widgetName)

    '''
    Table
    '''
    def cells_to_table(self, row, column):
        ''' add Row and Column to tableWidget '''
        self.widget.setRowCount(row)
        self.widget.setColumnCount(column)

    def checkbox_to_table(self, place):
        ''' add Checkbox to tableWidget '''
        self.check_box = QtGui.QCheckBox()
        self.widget.setCellWidget(place[0], place[1], self.check_box)

    def combobox_to_table(self, place, text):
        ''' add combobox to tableWidget '''
        self.comboBox = QtGui.QComboBox()
        #print str(self.widget.Name())
        self.comboBox.setObjectName("comboBox_table")
        for t in text:
            self.comboBox.addItem(QtGui.QApplication.translate("", t, None, QtGui.QApplication.UnicodeUTF8))

        self.widget.setCellWidget(place[0], place[1], self.comboBox)

    def labeltext_to_table(self, place, text):
        ''' singleline Text to tableWidget '''

        self.tableLabel = QtGui.QLabel()

        self.headerItem = QtGui.QTableWidgetItem()
        self.headerItem.setText(QtGui.QApplication.translate("TableEditor", "Partition", None, QtGui.QApplication.UnicodeUTF8))
        self.widget.setHorizontalHeaderItem(0,self.headerItem)

        self.headerItem = QtGui.QTableWidgetItem()
        self.headerItem.setText(QtGui.QApplication.translate("TableEditor", "Filesystem", None, QtGui.QApplication.UnicodeUTF8))
        self.widget.setHorizontalHeaderItem(1,self.headerItem)

        self.headerItem = QtGui.QTableWidgetItem()
        self.headerItem.setText(QtGui.QApplication.translate("TableEditor", "Format with", None, QtGui.QApplication.UnicodeUTF8))
        self.widget.setHorizontalHeaderItem(2,self.headerItem)

        self.headerItem = QtGui.QTableWidgetItem()
        self.headerItem.setText(QtGui.QApplication.translate("TableEditor", "Format", None, QtGui.QApplication.UnicodeUTF8))
        self.widget.setHorizontalHeaderItem(3,self.headerItem)

        self.headerItem = QtGui.QTableWidgetItem()
        self.headerItem.setText(QtGui.QApplication.translate("TableEditor", "UUID", None, QtGui.QApplication.UnicodeUTF8))
        self.widget.setHorizontalHeaderItem(4,self.headerItem)

        item = QtGui.QTableWidgetItem(str(text))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.widget.setItem(place[0], place[1], item)


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
