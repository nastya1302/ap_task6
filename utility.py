import concurrent.futures
import requests
import time
from random import randint

def download_images(link: str):
    response = requests.get(link)
    with open(f'image{randint(0,10)}.jpg', "wb") as f:
        f.write(response.content)
                                             
            
if __name__ == '__main__':
    t = time.time()
    links = input("Введите ссылки:")
    list_links = links.split()
    results = []
    for link in list_links:
        future = concurrent.futures.ProcessPoolExecutor().submit(download_images, link)
        results.append(future)
    print(time.time() - t)    