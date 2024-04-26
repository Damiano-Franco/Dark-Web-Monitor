import requests

session = requests.session()
session.proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
response = session.get("https://3g2upl4pq6kufc4m.onion/")
print(response)