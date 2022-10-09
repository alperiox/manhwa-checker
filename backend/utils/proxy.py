import os

import requests
import random

from dotenv import load_dotenv

load_dotenv()

PROXY_USERNAME = os.getenv("PROXY_USERNAME")
PROXY_PASSWORD = os.getenv("PROXY_PASSWORD")
PROXY_AUTH = os.getenv("PROXY_AUTH")

class StandardHTTPProxyRotator(object):
    def __init__(self):        
        response = requests.get(
            "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25",
            headers={"Authorization": f"Token {PROXY_AUTH}"},
        )
        self.proxies = response.json()['results']

    def __next__(self):
        self._check()
        proxy = random.choice(self.proxies)
        self.proxies.remove(proxy)
        return {"http": f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{proxy['proxy_address']}:{str(proxy['port'])}"}
    
    def __iter__(self):
        return self
    
    def _check(self):
        if len(self.proxies)==0:
            self.proxies = random.shuffle(self.response.json())