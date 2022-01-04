from typing import List, Dict
from time import sleep

from udemy.mercado.mercado.produto.produto import Produto
from udemy.mercado.mercado.util.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    opcao: int = int(input('===================================\n'
                           '=============bem vindo=============\n'
                           '=============GEEK SHOP=============\n'
                           '===================================\n'
                           'selecione uma opção abaixo:\n\n'
                           '1 - Cadastrar produto\n'
                           '2 - Listars produtos\n'
                           '3 - Comprar produto\n'
                           '4 - Visualizar carrinho\n'
                           '5 - Fechar pedido\n'
                           '6 - Sair\n'))
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('volte sempre')
        sleep(2)
        exit(0)
    else:
        print('opção invalida!')
        menu()


def cadastrar_produto() -> None:
    nome: str = input('CADASTRO DE PRODUTOS\n'
                      '======================\n'
                      'informe o nome do produto: ')
    preco: float = float(input('informe o preço: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {nome} foi cadastrado com sucesso')
    sleep(2)
    menu()


def listar_produto() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos\n'
              '--------------------')
        for produto in produtos:
            print(produto)
            print('------------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho:\n'
              '-------------------------------------------------------------\n'
              '=====================produtos disponiveis====================')
        for produto in produtos:
            print(produto)
            print('-------------------------------------------------------------')
            sleep(1)
        codigo: int = int(input())
        produto: Produto = pega_produto(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} possui {quant + 1} unidades no carrinho')
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'o produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                iten = {produto: 1}
                carrinho.append(iten)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos para vender')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'quantidade: {dados[1]}')
                print('-----------------------------------')
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'quantidade: {dados[1]}')
                valor_total = dados[0].preco * dados[1]
                print('-----------')
                sleep(1)
        print(f'sua fatura é {formata_float_str_moeda(valor_total)}\nvolte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho')
    sleep(2)
    menu()


def pega_produto(codigo: int) -> Produto:
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
            return produto
    return produto


if __name__ == '__main__':
    main()