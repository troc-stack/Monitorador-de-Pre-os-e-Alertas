import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

a = requests.get('https://www.mercadolivre.com.br/unidade-de-estado-solido-interna-m2-nvme-pcie-40-de-1-tb-de-alta/p/MLB2078472307#polycard_client=search-desktop&be_origin=backend&overlay_label=not_apply&search_layout=grid&position=1&type=product&tracking_id=f37ef3ef-161c-45da-a0ca-c4d3e3c0d754&wid=MLB7308047282&sid=search', headers)

print(a)
print(a.text)

if a.status_code == 200:
    print("Site acessado com sucesso imitando um navegador!")
elif a.status_code == 403:
    print('Bloqueado, acesso proibido')
elif a.status_code == 404:
    print('Página não encontrada')
elif a.status_code == 500:
    print('Erro no servidor do próprio sit')
else:
    print(f'Falha no acesso: {a.status_code}')