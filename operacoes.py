from persistencia_db import salvar_dados
from config import LIMITE_SAQUES

def ler_valor(mensagem):
    try:
        valor = float(input(mensagem))
        return valor
    except ValueError:
        print('Erro: digite apenas números!')
        return None

def ver_saldo(saldo):
    print(f"\nSeu saldo é: R$ {saldo:.2f}")

def depositar(saldo, historico, saques_realizados):
    valor = ler_valor('Digite o valor do depósito: R$ ')

    if valor is None:
        return saldo, historico, saques_realizados

    if valor > 0:
        saldo += valor
        historico.append(f'Depósito: +R${valor:.2f}')
        salvar_dados(saldo, historico, saques_realizados)
        print('Depósito realizado com sucesso!')
    else:
        print('Valor inválido!')

    return saldo, historico, saques_realizados

def sacar(saldo, historico, saques_realizados):
    valor = ler_valor('Digite o valor do saque: R$ ')

    if valor is None:
        return saldo, historico, saques_realizados

    if saques_realizados >= LIMITE_SAQUES:
        print('Limite de saques diários atingido!')
        return saldo, historico, saques_realizados

    if valor > 0 and valor <= saldo:
        saldo -= valor
        saques_realizados += 1
        historico.append(f'Saque: -R${valor:.2f}')
        salvar_dados(saldo, historico, saques_realizados)
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente ou valor inválido!')

    return saldo, historico, saques_realizados

def ver_extrato(saldo, historico, saques_realizados):
    print('\n=== EXTRATO ===')

    if len(historico) == 0:
        print('Nenhuma transação realizada.')
    else:
        for item in historico:
            print(item)

    print(f'\nSaldo atual: R${saldo:.2f}')
    print(f'Saques realizados hoje: {saques_realizados}/{LIMITE_SAQUES}')