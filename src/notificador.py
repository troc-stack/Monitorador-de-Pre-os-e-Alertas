import json

def notificador(): 
    try:
        with open("config.json", "r", encoding="utf-8") as arquivo: 
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('arquivo não encontrado!')

    for produto in dados['produtos']:
        if produto['preço_alvo'] >= x:
            pass # Notificar

        else: 
            pass #Não notificar 





