import time
import os

#Função para limpeza de terminal.

def limpar():
    os.system('cls')

# Definir as funções de soma, sub, multiplicação e adição.

def soma(x, y):
    s = x + y


def sub(x, y):
    s = x - y


def mult(x, y):
    s = x * y


def divisao(x, y):
    s = x / y


# Painel de escolhas do usuario.
print("------BEM VINDO A CALCULADORA DO JOÃOZINHO --------")
print('''Escolha a opção desejada:
[0] soma
[1] Subtração
[2] Multiplicação
[3] Divisão 
''')


# Codigo montado.

def calculadora():
    usuario = int(input("Digite a Opção desejada entre os números: "))

    for i in range(0, 20):

        if usuario >= 4 or usuario < 0:
            print('Só entre 0 e 3 irmão!!')
        else:
            pass

        print('\n')
        if usuario == 0:
            print('Opa, então você precisa somar??')
            print('\n')
            time.sleep(1)
            x = int(input('escolha o primeiro número: '))
            print('\n')
            y = int(input('Escolha o segundo número: '))
            print('\n')
            print('A Soma entre o número {} e o outro {} é = {}'.format(x, y, (x + y)))
            print('\n')
            soma(x, y)

        if usuario == 1:
            print('Opa, então você escolheu subtração??')
            print('\n')
            time.sleep(1)
            x = int(input('escolha o primeiro número: '))
            print('\n')
            y = int(input('Escolha o segundo número: '))
            print('\n')
            print('A Subtração entre o número {} e o outro {} é = {}'.format(x, y, (x - y)))
            print('\n')
            sub(x, y)

        if usuario == 2:
            print('Opa, então você escolheu Multiplicação??')
            print('\n')
            time.sleep(1)
            x = int(input('escolha o primeiro número: '))
            print('\n')
            y = int(input('Escolha o segundo número: '))
            print('\n')
            print('A Multiplicação entre o número {} e o outro {} é = {}'.format(x, y, (x * y)))
            print('\n')
            mult(x, y)

        if usuario == 3:
            print('Opa, então você escolheu Divisão??')
            print('\n')
            time.sleep(1)
            x = int(input('escolha o primeiro número: '))
            print('\n')
            y = int(input('Escolha o segundo número: '))
            print('\n')
            print('A divisão entre o número {} e o outro {} é = {}'.format(x, y, (x / y)))
            print('\n')
            divisao(x, y)

        # Caso o usuario queira jogar de novo.

        again = input('Você deseja continuar? [S/N]: ')
        print('\n')
        if again == 'S':
            return calculadora()
            return limpar()
        else:
            break
            print('Até a proxima!!')

calculadora()