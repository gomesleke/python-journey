'''
"Um número é um quadrado perfeito, ou um número quadrado, se ele for o quadrado de um inteiro positivo. Por exemplo, 25 é um número quadrado porque 5^2=5x5=25; ele também é um quadrado ímpar.

Os primeiros 5 números quadrados são: 1, 4, 9, 16, 25, e a soma dos quadrados ímpares é 1+9+25=35.

Entre os primeiros 514 mil números quadrados, qual é a soma de todos os quadrados ímpares?"
'''
i=0
for x in range(1,514001):
    square_x=x**2
    if x%2 !=0:
        i+=square_x

print(i)

