#!usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
#clear the screen
subprocess.call('clear', shell=True)

#ask for input 
print "Port Scanner programe written by Pawan. \n"
remoteServer = raw_input('Enter a remote host to scan:')
remoteServerIP = socket.gethostbyname(remoteServer)

# print a nice banner with information on which host we are about to scan
print "-"*60
print "Please wait, scanning remote host", remoteServerIP
print"-"*60

#check what time the scan started
t1 = datetime.now()

#using the range function to specify ports (here it will scans all teh port between 1 and 1024)
# we also put in same error handling for catching errors

try:
    for port in range(1,1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP,port))
        if result == 0:
            print " Port {}: Open".format(port)
        sock.close()
except KeyboardInterrupt:
    print "You pressed CTRL+C"
    sys.exit()
except socket.gaierror:
    print "Hostname could not be resolved. Exiting"
    sys.exit()

except socket.error:
    print"Could not connect to the server"
    sys.exit()

#checking the time again
t2 = datetime.now()
# caluculate the difference of time, to see how long it took to run the script
total = t2 -t1

# printing the information to screen
print "scanning complete in:", total
  

    