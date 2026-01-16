#some de dois números digitados pelo usuário
import os

def problem():
    try:
        os.system('cls')
        primeiro_numero_user=float(input('Digite um número: '))
        segundo_numero_user=float(input('Digite um número: '))

        soma=sum((primeiro_numero_user,segundo_numero_user))
        print(f'A soma é: {soma}')

    except ValueError:
        print('Ocorreu um erro, tente novamente!')
        input('Aperte uma tecla do teclado: \n')
        problem()

problem()

