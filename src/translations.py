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
class Gettxt(object):
    ''' translateable strings '''
    def __init__(self):
        print 'class Gettxt __init__'

    def not_found(self):
        return QtCore.QCoreApplication.translate("gettxt", "not found")
    def label_start(self):
        return QtCore.QCoreApplication.translate("gettxt", "This wizard will help you to install the live distribution.")


#
# start translation gui
#
class Gettxt_gui(object):
    def __init__(self, ui, MainWindow, app):
        print 'class Gettxt_gui __init__'

        self.ui = ui
        self.MainWindow = MainWindow
        self.app = app

    def gettxt_gui_run(self):
        '''
        MainWindow = QtGui.QMainWindow()
        load $LANG
        '''
        try:
            self.lang = os.environ["LANG"]
            #lang = str(QLocale.system().name())
        except:
            print "$LANG not found!"
            return

        if len(self.lang) < 2:
            return

        '''
        create .qm (translation file) filepath
        de, fr, pt, ...
        '''
        self.locale   = self.lang.split("_")
        self.path     = '%s%s' % (os.path.dirname(__file__), "/../ts")        # *.qm filepath
        self.progname = os.path.basename(sys.argv[0]).split(".")    # echo $0, without .py
        self.ts_file  = self.progname[0] + "_" + self.locale[0] + ".qm"

        ''' load translation file '''
        self.trans = QTranslator(self.app)
        self.app.installTranslator(self.trans)
        self.loaded = self.trans.load(self.ts_file, self.path)
        if not self.loaded:
            print '%s/%s not found!' % (self.path, self.ts_file)

        ''' translate now '''
        self.ui.retranslateUi(self.MainWindow)
