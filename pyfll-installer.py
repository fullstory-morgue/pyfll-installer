# -*- coding: utf-8 -*-

__author__    = 'Horst Tritremmel'
__copyright__ = '(C) 2008 Horst Tritremmel <hjt@sidux.com>'
__license__   = 'GPLv2 or any later version'

import os
import sys
from src.main import FLLInstaller

# files
CONF_FILE = "pyfll-installer.conf"


class Error(Exception):
    ''' A generic error handler that does nothing. '''
    pass


#
# main
#
'''
if __name__ == "__main__":
    try:
        if os.getenv("USER", default=None) != "root":
            print "Requires root!"
            sys.exit(1)

        else:
            fll = FLLInstaller(CONF_FILE)
            fll.main()
    except KeyboardInterrupt:
        pass
    except Error:
        sys.exit(1)
'''
fll = FLLInstaller(CONF_FILE)
fll.main()
