'''
Created on Sep 27, 2010

@author: Kyle
'''
import os, time, sys
from lib.children import Children

class Ppwn():
    
    NGINX = 'nginx.exe'
    PHP = 'php\\5.3\\php-cgi.exe'
    MYSQL = 'mysql\\bin\\mysqld.exe'
    PHP_ARGS = ['-b' , '127.0.0.1:9000', '-c' , r'C:\\nginx\\php\\5.3\\php.ini']
    
    def __init__(self, root_dir):
        # Setup the environment variables for the PHP FastCGI process 
        os.putenv('PHP_FCGI_CHILDREN', '4')
        os.putenv('PHP_FCGI_MAX_REQUESTS', '5000')
        
        # Change to the correct directory
        os.chdir(root_dir)
    
        # Determine the directory the script is running in
        if hasattr(sys, "frozen"):
            directory = os.path.dirname(unicode(sys.executable, sys.getfilesystemencoding( )))   
        else: 
            directory = os.path.dirname(unicode(__file__, sys.getfilesystemencoding( )))   
    
        # Create child processes
        self.child_processes = Children()
        self.child_processes.add('nginx', self.NGINX)
        self.child_processes.add('php', self.PHP, self.PHP_ARGS)
        self.child_processes.add('mysql', self.MYSQL)
    
    def restart(self):
        self.child_processes.restart_all()
       
    def __del__(self):
        self.child_processes.remove_all()
