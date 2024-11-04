import sys
import socket
import getopt
import threading
import subprocess

#se define algunas variables 

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


