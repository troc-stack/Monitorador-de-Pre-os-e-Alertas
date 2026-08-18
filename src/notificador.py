import json

def validar(x): 
    try:
        with open("config.json", "r", encoding="utf-8") as arquivo: 
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('arquivo não encontrado!')
        return []

    Notificar_produtos = []

    for produto in dados['produtos']:
        if produto['preco_alvo'] >= x:
            Notificar_produtos.append(produto.copy()) # Notificar
        else: 
            pass #Não notificar

    return Notificar_produtos

def menssagem():
    pass

def notificar(): 
    pass





