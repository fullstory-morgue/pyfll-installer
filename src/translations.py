#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__    = 'Horst Tritremmel'
__copyright__ = '(C) 2008 Horst Tritremmel <hjt@sidux.com>'
__license__   = 'GPLv2 or any later version'


import os , sys, locale
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QTranslator

#
# internationalisation strings
#
class Gettxt(QtCore.QObject):
    ''' translateable strings '''
    def not_found(self):
        return QtCore.QCoreApplication.translate("gettxt", "not found")
    def label_start(self):
        return QtCore.QCoreApplication.translate("gettxt", "This wizard will help you to install the live distribution.")


#
# start translation gui
#
class Gettxt_gui(object):
    def __init__(self, ui, MainWindow, app):
        self.ui = ui
        self.MainWindow = MainWindow
        self.app = app

    def gettxt_gui_run(self):
        '''
        MainWindow = QtGui.QMainWindow()
        load $LANG
        '''
        try:
            lang = os.environ["LANG"]
            #lang = str(QLocale.system().name())
        except:
            print "$LANG not found!"
            return

        if len(lang) < 2:
            return

        '''
        create .qm (translation file) filepath
        de, fr, pt, ...
        '''
        locale   = lang.split("_")
        path     = os.path.dirname(__file__) + "/../ts"        # *.qm filepath
        progname = os.path.basename(sys.argv[0]).split(".")    # echo $0, without .py
        ts_file  = progname[0] + "_" + locale[0] + ".qm"

        ''' load translation file '''
        trans = QTranslator(self.app)
        self.app.installTranslator(trans)
        loaded = trans.load(ts_file, path)
        if not loaded:
            print path + "/" + ts_file + " not found!"

        ''' translate now '''
        self.ui.retranslateUi(self.MainWindow)
