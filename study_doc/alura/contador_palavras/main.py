from contador import contar_palavras

texto_user=str(input('Escreva o seu texto: '))
quantidade=contar_palavras(texto_user)
print(f'A quantidade de palavras é: {quantidade}')
