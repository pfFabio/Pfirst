a = "0"
def testa_float(num1, num2):
    try:
        float(num1)
        float(num2)
        return True
    except ValueError:
        print('você não usou numeros')
        return False


def soma(a, b):
    return a+b


def sub(a, b):
    if a > b:
        return a-b
    if b > a:
        return -(b-a)


def mult(a, b):
    return a*b


def div(a, b):
    return a/b


while a != "":
    a = input("digite sua conta\n")
    if '+' in a:
        b, c = a.split('+')
        res = soma(float(b), float(c))
        print(res)
    elif '-' in a:
        b, c = a.split('-')
        res = sub(float(b), float(c))
        print(res)
    elif '*' in a:
        b, c = a.split('*')
        res = mult(float(b), float(c))
        print(res)
    elif '/' in a:
        b, c = a.split('/')
        res = div(float(b), float(c))
        print(res)
    b = res
