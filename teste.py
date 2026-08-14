import requests

a = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

print(a)
print(a.text)

if a.status_code == 200:
    print("Site acessado com sucesso imitando um navegador!")
else:
    print(f'Falha no acesso: {a.status_code}')