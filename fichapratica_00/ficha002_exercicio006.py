# Programa para somar os números de 1 a 100

def soma_um_ate_cem():
    list = []
    numero = 1

    while 1<=numero<=100:
        # print(numero)
        list.append(numero)
        numero += 1

    aux = 0

    for i in range(len(list)):
        aux = aux + list[i]
    return aux

print(soma_um_ate_cem())