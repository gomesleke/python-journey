from contador import contar_palavras
from contador import clean
import os

os.system('cls')
texto_user=str(input('Escreva o seu texto: '))
quantidade=contar_palavras(texto_user)
print(f'A quantidade de palavras é: {quantidade}')
