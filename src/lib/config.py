'''
Created on Oct 7, 2010

@author: Kyle
'''
import yaml, os, logging

log = logging.getLogger("ppwn.config")

class Config():
    
    CONFIG_FILE = '/conf.yaml'
    
    def __init__(self, directory):
        self.directory = directory
    
    def load(self):
        try:
            # Load the contents of the configuration file
            f = open(self.directory + self.CONFIG_FILE)
            contents = f.read()
            configuration = yaml.load(contents)
            f.close()
            
            # Validate the contents of the configuration file
            configuration = self.validate(configuration)
            return configuration
        except yaml.parser.ParserError:
            log.error("There was an error parsing the configuration file.")
            log.error("Please make sure it's in the correct format.")
        except IOError:
            log.error("Could not open the configuration file for the program.")
            log.error("File should be located at {0}" . format(self.directory + self.CONFIG_FILE))
            log.error("See the README.txt file for more information.")
          
    
    '''
    ' Validate the configuration data structure to make sure it has all the required properties.
    ' Will cause the configuration to be set to None if there is a missing property
    '''
    def validate(self, configuration):
        # Check that we have all the sections
        try:
            configuration['service']
            configuration['server']
            configuration['database']
        except KeyError as e:
            log.error("Your configuration is missing a section called {0}.".format(e)) 
        
        # Check that we have all of our service settings
        try:
            configuration['service']['interval']
        except KeyError as e:
            log.error("The service section in your configuration must have a setting in it called 'interval'.")
            return
        
        # Check that we have remote server settings
        try:
            configuration['server']['host']
            configuration['server']['remotepath']
        except KeyError as e:
            log.error("The server section in your configuration must have a setting in it called {0}.".format(e))
            return
        
        # Ensure that there is a keyfile set, or a username and password set
        if not ('keyfile' in configuration['server'] or ('username' in configuration['server'] and 'password' in configuration['server'])):
            log.error("You must have a keyfile or a username/password combination specified in your server configuration section.")    
        
        # Check that we have all database settings
        try:
            configuration['database']['host']
            configuration['database']['db']
            configuration['database']['username']
            configuration['database']['password']
        except KeyError as e:
            log.error("The database section in your configuration must have a setting in it called {0}.".format(e))
            return
        
        return configuration
