import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

a = requests.get('https://www.mercadolivre.com.br/unidade-de-estado-solido-interna-m2-nvme-pcie-40-de-1-tb-de-alta/p/MLB2078472307', headers=headers)


print("Status:", a.status_code)
print("URL:", a.url)
print("Tamanho:", len(a.text))
print("Content-Type:", a.headers.get("Content-Type"))

print(a.text[:2000])


print(f'Falha no acesso: {a.status_code}')