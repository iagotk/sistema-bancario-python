import json
import os
from config import ARQUIVO_DADOS

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados['saldo'], dados['historico'], dados['saques_realizados']
    else:
        return 0.0, [], 0

def salvar_dados(saldo, historico, saques_realizados):
    dados = {
        'saldo': saldo,
        'historico': historico,
        'saques_realizados': saques_realizados
    }

    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)