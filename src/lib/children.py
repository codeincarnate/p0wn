'''    
Created on Oct 7, 2010

@author: Kyle Cunningham <kyle@codeincarnate.com>
'''
import killableprocess, subprocess

class Children(object):
    '''
    The Children class manages a set of child processes.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.children = {}
        self.child_args = {} # Contains the arguments used to launch processes
    
    '''
    Add a child process.
    
    @param id: A string which is a unique idenfitier for the process.
    @param exe: A string which is the executable to run.
    @param args: A list of arguments.
    @param path: An optional path to where the executable is located.
                If this isn't set the current working directory will be used.
    '''    
    def add(self, id, exe, args = [], path = None):
        if id in self.children.keys():
            raise Exception('There is already a child process with that ID.')
    
        # Record the arguments used to launch the chld process    
        self.child_args[id] = {'exe': exe, 'args': args, 'path': path}
        
        # Set the correct path
        if not path:
            exe_path = exe
        else:
            exe_path = path + exe
        
        # Merge arguments
        full_args = [exe_path] + args 
        
        # Launch process    
        self.children[id] = killableprocess.call(full_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    
    '''
    Terminate a child process, and then start it again
    '''
    def restart(self, id):
        restart_args = self.child_args[id]
        self.children[id].kill()
        del self.children[id]
        
        self.add(id, restart_args['exe'], restart_args['args'], restart_args['path'])
    
    '''
    Terminate all child processes then start them again
    '''
    def restart_all(self):
        children = self.children
        for id in children.keys():
            self.restart(id)
        
    '''
    Terminate a child process
    
    @param id: The unique identifier of the process.
    '''    
    def remove(self, id):
        self.children[id].kill()
        del self.children[id]
        del self.child_args[id]
    
    
    '''
    Terminate all child processes
    '''
    def remove_all(self):
        for id in self.children.iterkeys():
            self.children[id].kill()
        self.children.clear()