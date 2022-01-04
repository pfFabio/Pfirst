a = 0
print('bem vindo a minha calculadora')


def testa_float(num1, num2):
    try:
        float(num1)
        float(num2)
        return True
    except ValueError:
        print('você não usou numeros')
        return False


while a != "":
    a = input("digite sua conta\n")
    if '-' in a:
        c, d = a.split('-')
        if testa_float(c, d):
            print(float(c)-float(d))
    elif '+' in a:
        c, d = a.split('+')
        if testa_float(c, d):
            print(float(c)+float(d))
    elif '*' in a:
        c, d = a.split('*')
        if testa_float(c, d):
            print(float(c) * float(d))
    elif '/' in a:
        c, d = a.split('/')
        if testa_float(c, d):
            print(float(c) / float(d))
