import random


def cria_equacoes(nivel: int) -> tuple:
    o: str = ''
    nivel = nivel * 2
    i = 1
    while i < nivel:
        if i%2 == 0:
            op = random.randint(1, 3)
            if op == 1:
                op = '+'
            elif op == 2:
                op = '-'
            elif op == 3:
                op = '*'
            o += op
        else:
            o += str(random.randint(0, 100))
        i += 1
    print(o)
    print(eval(o))



    #print(equacao)
    #print(eval(equacao))
    return o, int(eval(o))
