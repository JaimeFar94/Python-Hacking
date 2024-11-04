import requests
from bs4 import BeautifulSoup


def main():
    url ="http://arrendaautos.com/"
    cabecera = {'User-Agent':'Brave'}
    peticion = requests.get(url=url, headers=cabecera)
    soup = BeautifulSoup(peticion.text,'html5lib')
    for v in soup.find_all('meta'):
        if v.get('name') == 'generator':
            version = v.get('content')
    print(version)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Salir")
        exit()