# FastAPI Currency Converter API

Esta é uma API de conversão de moeda construída com FastAPI. A API permite converter uma quantia de uma moeda para várias outras moedas usando a API AlphaVantage.

## Instalação e Configuração

1. Clone o repositório:

```shell
git clone https://github.com/imWadson/currency-converter-API.git
cd currency-converter-API
```
2. Instale as dependências e crie um ambiente virtual com Poetry:

```shell
poetry install
```

## Uso
```shell
 ##exempli de uso da rota /converter/
 import request

 response = requests.get('http://localhost:8000/converter/USD', json={"to_currencies": ["EUR", "GBP"], "price": 100})
 print(response.json())
```