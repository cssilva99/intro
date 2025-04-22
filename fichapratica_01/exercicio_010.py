# Escreva um programa que leia dois números reais 
# e pergunte ao utilizador qual a operação aritmética 
# que pretende realizar e apresente o resultado

# O utilizador deve responder usando o simbolo da operação

numero1 = int(input("Digite um número real: "))
numero2 = int(input("Digite outro número real: "))
operador = str(input("Digite o operador do cálculo que pretende efetuar : "))

if operador == "+" :
    print("Resultado : ".join(numero1 + numero2))
elif operador == "-":
    print("Resultado : ".join(numero1 - numero2))
elif operador == "*":
    print("Resultado : ".join(numero1 * numero2))
elif operador == "/":
    print("Resultado : ".join(numero1 / numero2))
else:
    print("Invalid Operator")