# Monitorador de Preços e Alertas (Price Tracker & Alert)

## O que faz?
 Um script/bot usando **Python** que entra em sites de e-commerce (Mercado Livre, Amazon, etc.), raspa o preço de produtos específicos configurados por você e, quando o preço cai abaixo de um valor x, envia uma notificação automática (via e-mail ou mensagem no Telegram/Discord).
	
## Price Tracker
    - [ ] 'main.py' -> Cod principal responsavel pelo loop 
    - [ ] 'config.json' -> armazenamento dos dados de preços
    - [ ] 'scraper.py' -> Cod responsavel por realiar a raspagen de preço
    - [ ] 'notificador.py' -> Cod responsavel por realizar a notificação caso o preço abaixe