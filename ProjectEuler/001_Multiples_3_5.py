i=0
for x in range(1,10):

    if x%3==0:
        i+=x
        print(x)
    elif x%5==0:
        i+=x
        print(x)
    else:
        pass

print(f'multiplos de 5 e 3 abaixo de 10: {i}')