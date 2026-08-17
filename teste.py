import requests

acesses = 'tG083bF4SVd6YYXm9yMxL4ZkTHkEGopS'

url = f"https://api.mercadolibre.com/items/MLB2078472307"

headers = {
    "Authorization": f"Bearer {acesses}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

a = requests.get(url, headers=headers)


print("Status:", a.status_code)
print("URL:", a.url)
print("Tamanho:", len(a.text))
print("Content-Type:", a.headers.get("Content-Type"))

print(a.text[:2000])