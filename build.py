#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__    = 'Horst Tritremmel'
__copyright__ = '(C) 2008 Horst Tritremmel <hjt@sidux.com>'
__license__   = 'GPLv2 or any later version'

import os

commands = \
    ("pyuic4 -o src/ui_mainwindow.py ui/mainwindow.ui",
    "pylupdate4 pyfll-installer.pro",
    "pyrcc4 -o res_rc.py ui/res.qrc")

for command in commands:
    print command
    os.system(command)
