from typing import List
from time import sleep

from udemy.banco.models.cliente import Cliente
from udemy.banco.models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    opcao = int(input('==========================\n'
                      '============ATM===========\n'
                      '=========GEEK BANK========\n'
                      '==========================\n'
                      'Selecione uma opção no menu:\n'
                      '1 - criar conta\n'
                      '2 - Efetuar saque\n'
                      '3 - Efetuar depósito\n'
                      '4 - Efetuar transferencia\n'
                      '5 - Listar contas\n'
                      '6 - Sair\n'))
    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('\nVolte sempre!')
        exit(0)
    else:
        print('opção inválida!')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('informe os dados do cliente')
    nome: str = input('Nome do cliente:')
    email: str = input("Email do cliente:")
    cpf: str = input('CPF do cliente:')
    data_nascimento: str = input('Data de nascimento do cliente:')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso\n'
          'dados da conta: \n'
          '----------------------')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('informe o numero da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('informe o valor do saque:'))

            conta.sacar(valor)
        else:
            print('a conta informada não foi encontrada')

    else:
        print('nenhuma conta está registrada')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        num: int = int(input('informe o número da sua conta:'))
        conta: Conta = buscar_conta_por_numero(num)
        if conta:
            conta.depositar(float(input('informe o valor a ser depositado:')))
        else:
            print('a conta informada não foi encontrada')
    else:
        print('nenhuma conta está registrada')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        num_o: int = int(input('informe o número da conta origem:'))
        conta_o: Conta = buscar_conta_por_numero(num_o)
        if conta_o:
            num_a: int = int(input('informe o número da conta destino:'))
            conta_a: Conta = buscar_conta_por_numero(num_a)
            if conta_a:
                conta_o.transferir(conta_a, float(input('informe o valor a ser transferido:')))
            else:
                print('a conta destino não foi encontrada')
        else:
            print('a conta origem não foi encontrada')
    else:
        print('nenhuma conta está registrada')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas:')
        for conta in contas:
            print(conta)
            print('--------------------------')
            sleep(1)
    else:
        print('não há contas registradas')
    sleep(2)
    menu()


def buscar_conta_por_numero(num: int) -> Conta:
        for conta in contas:
            if conta.numero == num:
                return conta



if __name__ == '__main__':
    main()
