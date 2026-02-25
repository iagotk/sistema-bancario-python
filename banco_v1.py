print()''=== SISTEMA FINANCEIRO BÁSICO ===')
while True:
      print('\n1 - Adicionar receita: ')
      print('2 - Adicionar despesa: ')
      print('3 - Ver saldo: ')
      print('4 - Sair')
      if opcao == '1':
            valor = float(input('Digite o valor da despesa: R$ '))
            saldo += valor
            print('Receita adicionada com sucesso!')
        elif opcao =='2':
            valor = float(input('Digite o valor da despesa: R$ '))
            saldo -= valor
            print('Despesa registrada')
        elif opcao == '3':
        print(f'Seu saldo atual é: R$ {saldo:.2f}')
        elif opcao =='4':
            print('Encerrando o sistema...')
            break
      else:
            print('Opçao inválida. Tente novamente.')


