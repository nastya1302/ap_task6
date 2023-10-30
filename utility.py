import concurrent.futures
import requests
import time
import sys
from random import randint

def download_images(link: str) -> None:
    response = requests.get(link).content
    with open(f'image{randint(0,10)}.jpg', "wb") as f:
        f.write(response)
                                             
            
if __name__ == '__main__':
    t = time.time()
    links = sys.argv[1:]
    results = []
    for link in links:
        future = concurrent.futures.ProcessPoolExecutor().submit(download_images, link)
        results.append(future)
    print(time.time() - t)    