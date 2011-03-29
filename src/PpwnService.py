'''
Created on Oct 7, 2010

@author: Kyle Cunningham <kyle@codeincarnate.com>
'''
import win32serviceutil, win32service, win32event, win32api
from ppwn import Ppwn

class PpwnService(win32serviceutil.ServiceFramework):
    '''
    A windows service for Ppwn
    '''
    _svc_name_ = 'Ppwn'
    _svc_display_name_ = 'Ppwn'

    def __init__(self, args):
        '''
        Constructor
        '''
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
    
    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        self.ppwn = Ppwn('C:\\nginx\\')
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)
        
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        del self.ppwn
        win32event.SetEvent(self.stop_event)
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)
        