#1 Concatenando Dados

str1 = input()
str2 = input()

def concatena(str1, str2):
    return str1 + str2

print(concatena(str1, str2))

#2 Repetindo Textos

str = input()
vezes = int(input())

def papagaio(str, vezes):
    for i in range(vezes):
        print(str)

#3 Operações Matemáticas Simples

a = float(input("insira um número: "))
b = float(input('insira outro número: '))
op = input('Qual operação deseja fazer? (+, -, *, /)')

match(op):
    case(+): print(a+b)
    case(-): print(a-b)
    case(*): print(a*b)
    case(/): if(b == 0):
        print('Operação Inválida')
        else: print(a/b)
