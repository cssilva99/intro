# Programa que exibe os 5 números anteriores e os 5 números seguintes a um número lido

numero = int(input("Digite um número : "))

menor = numero - 5
maior = numero + 5

while menor<=maior:
    print(menor)
    menor += 1

print("O maior é \n")
print(maior)