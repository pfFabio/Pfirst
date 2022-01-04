from equações import cria_equacoes

menu: str = '0'
pontos: int = 0


def checa(resposta, resultado):
    if resposta == resultado:
        print('parabens voce acertou e ganhou 1 ponto!\n')
        return 1
    else:
        volta = input('parece que vc errou digite 1 para tentar novamente ou 2 para voltar ao menu:\n')
        if volta == 1:
            checa(resposta, resultado)
        elif volta == 2:
            return 0


def jogar(nivel):
    equacao, resultado = cria_equacoes(nivel)
    resposta = int(input(f'qual o resultado dessa equacao:\n{equacao}\n'))
    return checa(resposta, resultado)


print('bem vindo ao meu jogo')

while menu != '3':
    menu = input('menu:\n1-jogar\n2-pontos\n3-sair\n')
    if menu == '3':
        break
    elif menu == '2':
        print(f'voce tem {pontos} pontos!\n')
    elif menu == '1':
        pontos += jogar(int(input('digite a quantidade de numeros na operação:')))
    else:
        print('você não digitou uma opção valida')
