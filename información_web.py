import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="Detector de Paginas Web")
    parser.add_argument('-t', '--target', help="Objetivo")
    args = parser.parse_args()

    if args.target:
        try:
            response = requests.get(url=args.target)
            web_headers = dict(response.headers)
            for key, value in web_headers.items():
                print(f"{key} : {value}")
        except requests.RequestException as e:
            print(f"No fue posible llegar al objetivo: {e}")
    else:
        print("No se encuentra el objetivo")

if __name__ == '__main__':
    main()
