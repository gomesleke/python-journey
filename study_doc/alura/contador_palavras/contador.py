def clean(texto):
    texto=texto.lower()
    caracteres=',.;/|\!@#$%¨&*()[]{}?°ª=+'
    for char in caracteres:
        texto=texto.replace(char,"")
    return texto


def contar_palavras(frase):
    frase=clean(frase)
    if not frase.strip(): #.strip() remove espaço --  mas essa parte siginifica se não houver nada valido, ele retorna nada
        return {}
    palavras=frase.split()
    contagem={}

    for palavra in palavras:
        contagem[palavra]=contagem.get(palavra,0)+1 #sistema que impede contar a mesma palavra masi de uma vez


    return contagem
