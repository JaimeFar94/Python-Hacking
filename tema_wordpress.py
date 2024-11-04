import requests
from bs4 import BeautifulSoup

def main():
    agent = {'User-Agent':'Brave'}
    peticion = requests.get(url="http://arrendaautos.com/",headers=agent)
    soup = BeautifulSoup(peticion.text,'html5lib')
    for enlace in soup.find_all('link'):
        if '/wp-content/themes' in enlace.get('href'):
            the = enlace.get('href')
            the = the.split('/')
            if 'themes' in the:
                pos = the.index('themes')
                theme = the[pos+1]
                print("El Tema Vulnerable es: " + theme)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit() 