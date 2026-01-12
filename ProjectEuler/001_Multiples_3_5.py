i=0
for x in range(1,1000):

    if x%3==0:
        i+=x
    elif x%5==0:
        i+=x
    else:
        pass

print(f'multiplos de 5 e 3 abaixo de 1000: {i}')