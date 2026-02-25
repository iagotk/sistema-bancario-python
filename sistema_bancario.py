saldo  = 0.0

while True:
    print('\n=== BANCO NEPRÉ ===')
    print('1 - Ver saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Sair')
    
    opcao = input('Escolha uma opçao: ')

    if opcao =='1':
        print(f'Seu saldo atual é: R$ {saldo:2f}')

    elif opcao =='2':
        valor = float(input('Digite o valor do depósito: R$ '))
        if valor > 0:
            saldo += valor
            print('Depósito realizado com sucesso!')
        else:
            print('Valor inválido!')
    elif opcao == '3':
        valor = float(input('Digite o valor do saque: R$ '))
        if valor <= saldo and valor > 0:
            saldo -= valor
            print('Saque realizado com sucesso!')
        else:
            print('Saldo insuficiente ou valor inválido!')
    elif opcao =='4':
        print('Encerrando o sistema...')
        break

    else:
        print('Opção inválida! Tente novamente.')
    