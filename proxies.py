import requests

proxies = [
    "http://82.179.94.11:3128",
    "http://13.83.94.137:3128",
    "http://177.234.241.25:999",
    "http://178.48.68.61:18080"
]
url = "https://api.ipify.org/"

for proxy in proxies:
    r = requests.get(url, proxies={"https": proxy})
    print(r.text)

