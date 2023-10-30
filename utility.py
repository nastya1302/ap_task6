import concurrent.futures
import requests
from PIL import Image
from io import BytesIO


def download_images(list_links: str):
    for i,link in enumerate(list_links):
        response = requests.get(link)
        f = open(f'image{i+1}.jpg', "wb")
        f.write(response.content)
        f.close()                                         
            

if __name__ == '__main__':
    links = input("Введите список ссылок: ")
    list_links = links.split()
    download_images(list_links)