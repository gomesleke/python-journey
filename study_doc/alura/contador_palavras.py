'''
contar as palavras

passos:
1-entrada e processamento
2-sistema de contagem
3-exibir
4-otimizar
'''
texto_user=str(input('Escreva o seu texto: '))

palavras=texto_user.split() #basicamente ele separa cada palavra e coloca em uma lista

contador=len(palavras)

print(contador)