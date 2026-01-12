'''
"Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou 5, obtemos 3, 5, 6 e 9. A soma desses múltiplos é 23. Encontre a soma de todos os múltiplos de 3 ou 5 abaixo de 1000."
'''
i=0
for x in range(1,1000):

    if x%3==0:
        i+=x
    elif x%5==0:
        i+=x
    else:
        pass

print(f'multiplos de 5 e 3 abaixo de 1000: {i}')