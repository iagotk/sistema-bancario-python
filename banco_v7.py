from persistencia_db import carregar_dados
from operacoes import ver_saldo, depositar, sacar, ver_extrato
from menu import mostrar_menu

saldo, historico, saques_realizados = carregar_dados()

while True:
    mostrar_menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        ver_saldo(saldo)

    elif opcao == '2':
        saldo, historico, saques_realizados = depositar(
            saldo, historico, saques_realizados
        )

    elif opcao == '3':
        saldo, historico, saques_realizados = sacar(
            saldo, historico, saques_realizados
        )
    elif opcao == '4':
        ver_extrato(saldo, historico, saques_realizados)

    elif opcao == '5':
        print('Encerrando o sistema...')
        break

    else:
        print('Opção inválida!')