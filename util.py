# -*- coding: utf-8 -*-

from sys import version_info
import os
import platform

py_version = version_info[0]

SIGNATURE = '''+----------------------------------------------+
|       CoDeD By 1337r00t (@0x1337r00t)        |
|             Blackfox's Group ©               |
|----------------------------------------------|
|  Arabic Tags [Windows(CMD)]: only urlencode  |
|             TrendCatch © 2019                |
+----------------------------------------------+
'''

def init():
    os.system('cls||clear')
    os.system('export PYTHONIOENCODING=utf-8')
    print(SIGNATURE)

def uinput(m): 
    return raw_input(m) if py_version == 2 else str(input(m))
