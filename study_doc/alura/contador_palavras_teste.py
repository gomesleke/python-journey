'''
contar as palavras

passos:
1-entrada e processamento
2-sistema de contagem
3-exibir
4-otimizar
'''
import os
os.system('cls')
def contar_palavras(texto):

    palavras=texto.split() #basicamente ele separa cada palavra e coloca em uma lista
    return len(palavras)

texto_user=str(input('Escreva o seu texto: '))

print(f'A quantidade de palavras é: {contar_palavras(texto_user)}')
