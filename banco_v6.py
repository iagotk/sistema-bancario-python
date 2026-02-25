import json
import os

ARQUIVO_DADOS = 'dados_banco.json'
LIMITE_SAQUES = 3

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados['saldo'], dados['historico'], dados['saques_realizados']
    else:
        return 0.0,[], 0
    
def salvar_dados(saldo, historico, saques_realizados):
    dados = {
        'saldo': saldo,
        'historico': historico,
        'saques_realizados': saques_realizados
    }
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

saldo, historico, saques_realizados = carregar_dados()

def ler_valor(mensagem):
    try:
        valor = float(input(mensagem))
        return valor
    except ValueError:
        print('Erro: digite apenas números!')
        return None
    
def ver_saldo():
    print(f'Seu saldo é: R${saldo:.2f}')

def depositar():
    global saldo
    valor = ler_valor('Digite o valor do depósito: R$ ')

    if valor is None:
        return
    
    if valor > 0:
        saldo += valor
        historico.append(f'Depósito: +R${valor:.2f}')
        salvar_dados(saldo, historico, saques_realizados)
        print('Depósito realizado com sucesso!')
    else:
        print('Valor inválido!')

def sacar():
    global saldo, saques_realizados
    valor = ler_valor('Digite o valor do saque: R$ ')

    if valor is None:
        return
    
    if saques_realizados >= LIMITE_SAQUES:
        print('Limite de saques diários atingido!')
        return
    if valor > 0 and valor <= saldo:
        saldo -= valor
        saques_realizados += 1
        historico.append(f'Saque: -R${valor:.2f}')
        salvar_dados(saldo, historico, saques_realizados)
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente ou valor inválido!')

def ver_extrato():
    print('\n=== EXTRATO ===')

    if len(historico) == 0:
        print('Nenhuma transação realizada.')
    else:
        for item in historico:
            print(item)

    print(f'\nSaldo atual: R${saldo:.2f}')
    print(f'Saques realizados hoje: {saques_realizados}/{LIMITE_SAQUES}')

while True:
    print('\n=== BANCO NEPRÉ V6 ===')
    print('1 - Ver saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Ver extrato')
    print('5 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        ver_saldo()

    elif opcao == '2':
        depositar ()

    elif opcao == '3':
        sacar()

    elif opcao == '4':
        ver_extrato()

    elif opcao == '5':
     print('Encerrando o sistema...')
     break

    else:
        print('Opção inválida!')



