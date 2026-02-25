saldo = 0.0
historico = []

while True:
    print('\n=== BANCO NEPRÉ V2 ===')
    print('1 - Ver saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Ver extrato')
    print('5 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao =='1':
        print(f'Seu saldo atual é: R$ {saldo:2.f}')
    elif opcao =='2':
        valor = float(input('Digite o valor do depósito: R$ '))
        if valor > 0:
            saldo += valor
            historico.append(f'Depósito: +R$ {valor:;2f}')
            print('Depósito realizado com sucesso!')
        else:
            print('Valor inválido!')
    elif opcao =='3':
        valor = float(input('Ditite o valor do saque: R$ '))
        if valor <= saldo and valor > 0
        saldo -= valor
        historico.append(f'Saque: -R$ {valor:.2f}')
        print('Saque realizado com sucesso!')
        else:
        print('Saldo insuficiente ou valor inválido!')
    elif opcao =='4':
        print('\n=== EXTRATO ===')
        if len(historico) == 0:
            print('Nenhuma transação realizada.')
        else:
            for item in historico:
                print(item)
    elif opcao =='5':
        print('Encerrando o sistema...')
        break

    else:
        print('Opção inválida!')
        

              
