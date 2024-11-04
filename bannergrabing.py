import socket 
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target', help='Indicar la ip de la victima') 
args = parser.parse_args()

def banner(ip,port):
    s = socket.socket()
    s.connect((ip,port))
    print(str(s.recv(1024)))

def main():
    if args.target:
        ip = args.target
        port = 21
        banner(ip,port)
    else:
        print("(-) Indica una ip")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
