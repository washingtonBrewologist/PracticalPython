#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the current screen
subprocess.call('clear', shell=True)

# Get user input
targetServer = raw_input("Enter a remote host to scan: ")
remoteServerIP= socket.gethostbyname(targetServer)

# Print banner with information on the host we're scanning
print '-'*60
print "Now Scanning Target ", remoteServerIP
print '-'*60

# Check scan start time
t1 = datetime.now()

# Using the range function to specify the ports we are scanning, also includes error handling
try:
   for port in range(1, 1025):
       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       result = sock.connect_ex((remoteServerIP, port))
       if result == 0:
           print "Port {}: Open".format(port)
       sock.close()
except KeyboardInterupt:
  print "You pressed Ctrl+C!"
  sys.exit()
except socket.gaierror:
  print 'Hostname could not be resolved! Now Exiting'
  sys.exit()
except socket.error:
  print "Couldn't connect to the target server!"
  sys.exit()

#Check the time again
t2 = datetime.now()

# Calculates the differences in time to get the total time needed to complete the scan!
total = t2 - t1
print 'Scanning of the target completed in: ', total

