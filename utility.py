import concurrent.futures
import requests
import time
import sys
from random import randint

def download_images(link: str) -> None:
    response = requests.get(link).content
    with open(f'image{randint(0,100)}.jpg', "wb") as f:
        f.write(response)
                                             
def main() -> None:
    t = time.time()
    links = sys.argv[1:]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        [executor.submit(download_images, link) for link in links]
    print(time.time() - t)   

if __name__ == '__main__':
    main()