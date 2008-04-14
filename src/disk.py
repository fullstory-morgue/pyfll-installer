# -*- coding: utf-8 -*-

__author__    = 'Horst Tritremmel'
__copyright__ = '(C) 2008 Horst Tritremmel <hjt@sidux.com>'
__license__   = 'GPLv2 or any later version'

import os
import commands

PROC_PARTITIONS = '/proc/partitions'
SYS_BLOCK       = '/sys/block'
UDEVINFO_CMD    = 'udevinfo --query=env --name='


class Diskinfo(object):
    def partitions(self):
        '''
        open and read procfile
        get procnames = ['sda', 'sda1', 'sdb', 'sdb1', ... ]
        '''
        self.procfile = open(PROC_PARTITIONS, 'r')
        self.procnames = [ '/dev/%s' % (self.p.split()[3]) for self.p in self.procfile.readlines()[2:] ]
        self.procfile.close()

        return self.procnames


    def udevinfo(self, device):
        '''
        get disk or partition info
        INFO: get all keys from udevinfo      Diskinfo().udevinfo('/dev/sda1').keys()
        '''
        self.device = device.split('/')[2]
        self.dict_udevinfo = {}
        self.dict_udevinfo.clear()

        ''' top-level device path /sys/block (for disk or partiton) '''
        self.sysblock = os.listdir(SYS_BLOCK)


        if self.device in self.sysblock:
            ''' disk '''
            self.dict_udevinfo['TYP'] = 'disk'
        else:
            ''' partition '''
            self.dict_udevinfo['TYP'] = 'partition'

        ''' start udevinfo comand '''
        self.udevinfo = commands.getoutput("%s%s" % (UDEVINFO_CMD, self.device)).split('\n')
        ''' split udevinfo and create dict '''
        for self.u in self.udevinfo:
            self.v = self.u.split('=')
            self.dict_udevinfo[self.v[0]] = self.v[1]

        return self.dict_udevinfo
