from ..backend.utils.proxy import StandardHTTPProxyRotator
import requests

def test_StandardHTTPProxyRotator():
    rotator = StandardHTTPProxyRotator()
    url = "http://ident.me/"
    current_ip = requests.get(url)
    proxy_ip = requests.get(url, proxies=next(rotator))
    assert proxy_ip != current_ip