import subprocess
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target', help='Indicar la url \n(e.g https://ejemplo.com)') 
args = parser.parse_args()

def main():
    if args.target:
        subprocess.call("wad -u " + args.target + "> tecnologias.txt", shell=True)

        tecnologias = open("tecnologias.txt", 'r')
        tecnologias= tecnologias.read()
        tecnologias = tecnologias.split("[")
        tecnologias = tecnologias[1].split("]")
        tecnologias = tecnologias[0].split('{')


        for tecnologia in tecnologias:
            nuevo = tecnologia.replace('\n','')
            nuevo =  nuevo.replace('                                                   ','')
            nuevo = nuevo.replace('"','')
            nuevo = nuevo.split('}')
            nuevo = nuevo[0]
            nuevo = nuevo.replace(',','\n')

            print(nuevo)
            print("*"*20)




    else:
        print("(-) Ingresa una URL")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
