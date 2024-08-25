import requests

PAGBANK_API_URL = 'https://api.pagbank.com.br'
PAGBANK_API_KEY = 'sua_chave_api_aqui'

def criar_pagamento(valor, email_usuario):
    endpoint = f'{PAGBANK_API_URL}/pagamentos'
    headers = {
        'Authorization': f'Bearer {PAGBANK_API_KEY}',
        'Content-Type': 'application/json',
    }
    dados = {
        'valor': valor,
        'email_usuario': email_usuario,
    }
    resposta = requests.post(endpoint, headers=headers, json=dados)
    return resposta.json()
