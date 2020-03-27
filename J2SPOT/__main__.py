"""
J2SPOT-"!!!The Honeypot !!!"

Simple TCP honeypot logger by team J2SPOT[Janan(68),Joshua(69),Sharoz(96)]

Usage:
    
  JS2POT <config_filepath>

Options:
  
    <config_filepath>  Path to config options file
  
    -h --help     Show this screen.
 """
import configparser
import sys
#import logging
from J2SPOT import HoneyPot
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)
#craeting an alternate way to print the documentation


#def print_usage():
#    print("usage: ")
#    print(" python -m J2SPOT /lee/mini_project/J2SPOT.ini")

#check arguments 
if len(sys.argv) < 2 or sys.argv[1] in ['-h','--help']:
  #  print("[-] Not enough arguments....")
    print(__doc__)
    sys.exit(1)


#Lodad config    
    
config_filepath=sys.argv[1]


#config_filepath='/etc/J2SPOT.ini'
config=configparser.ConfigParser()
config.read(config_filepath)
ports = config.get('default','ports',raw=True,fallback="8080,8888,9999")
hosts = config.get('default','hosts',raw=True,fallback="0.0.0.0")
log_filepath = config.get('default','logfile',raw=True,fallback="/var/log/J2SPOT.log")
#logger.info("[*]Ports:%s"%ports)
#logger.info("[*]Logfile: %s"%log_filepath)

#checkimg the provided ports
ports_list=[]

try:
    ports_list = ports.split(',')
except Exception as e:
    print('Error  pasing ports:%s \n Exiting',ports )
    sys.exit(1)
    
    
#come lets launch the honeypot
honeypot = HoneyPot(hosts, ports_list,log_filepath)
honeypot.run()


#from docopt import docopt
  
#args=docopt(__doc__) 
  
#print("Config file:%s",args['[config_filepath]'])
  # -*- coding: utf-8 -*-

