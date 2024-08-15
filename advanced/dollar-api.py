import requests
req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
reqJson = req.json()


dolar = round(float(reqJson["USDBRL"]['bid']), 2)
print(f'O dólar agora está R$ {dolar:.2f}')


        