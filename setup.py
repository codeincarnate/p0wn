'''
Created on October 7, 2010

@author: Kyle Cunningham <kyle@codeincarnate.com>
'''

# Setup basic information
NAME = 'Ppwn'
DESCRIPTION = 'Run nginx, PHP, and PostgreSql together.'
COPYRIGHT = '(c) 2010, Code Incarnate Technologies'
COMPANY = 'Code Incarnate Technologies'
VERSION = '1.00.00'

from distutils.core import setup
import sys, os, glob, shutil, py2exe
sys.path.insert(0,os.getcwd() + '\src')

def getFiles(dir):
        # dig looking for files
        a= os.walk(dir)
        b = True
        filenames = []
        while (b):
                try:
                        (dirpath, dirnames, files) = a.next()
                        filenames.append([dirpath, tuple(files)])
                except:
                        b = False
        return filenames


print 'Creating windows service...'
setup(
    name = NAME,
    description = DESCRIPTION,
    version = VERSION,
    service = [{'modules':["PpwnService"], 'cmdline':'pywin32'}],
    zipfile = None,
    options = {
                    "py2exe":{"packages": ["win32api"],
                              "includes": "win32com,win32service,win32serviceutil,win32event",
                              "optimize": '2',
                              "bundle_files": 1,
                              'dll_excludes': [ "mswsock.dll", "powrprof.dll" ],
                            },
                    },                         
)
 