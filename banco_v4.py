saldo = 0.0
historico []

def ver_saldo():
    print(f'Seu saldo é: R${saldo:.2f}')

def depositar():
    global saldo
    valor = float(input('Digite o valor do depósito: R$'))

    if valor > 0:
        saldo += valor
        historico.append(f'Depósito: +R${valor:.2f}')
        print('Depósito realizado com sucesso!')
    else:
        print('Valor inválido!')

def sacar
    global saldo
    valor = float(input('Digite o valor do saque: R$ '))

    if valor > 0 and valor <= saldo:
        saldo -= valor
        historico.append(f'Saque: -R$ {valor:.2f}')
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente ou valor inválido!')

def ver_extrato()
    print('\n=== EXTRATO ===')
    if len(historico) == 0
        print('Nenhuma transação realizada.')
    else:
        for item in historico:
             print(item)

while True:
    print('\n=== BANCO NEPRÉ V3 ===')
    print('1 - Ver saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Ver extrato')
    print('5 - Sair')

    opcao = input('Escolha uma opção:')

    if opcao == '1':
        ver_saldo()
          
    elif opcao =='2':
        depositar()

    elif opcao =='3':
        sacar()
    
    elif opcao == '4':
        ver_extrato()

    elif opcao =='5':
        print('Encerrando o sistema...')
        break

    else:
        print('Opção inválida!')
        



