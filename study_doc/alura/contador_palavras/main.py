from contador import contar_palavras
from contador import clean
import os

os.system('cls')
texto_user=(str(input('Escreva o seu texto: '))).strip()

if not texto_user:
    print('Você não inseriu um texto.')
else:

    resultado=contar_palavras(texto_user)

    if resultado:
        print('Contagem:')
        for palavra,quantidade in resultado.items():
            print(f' - {palavra}:{quantidade}')
    else:
        print('Não há palavra válida')
