# Escrever um programa que calcula a média aritmética de 3 números informados pelo utilizador
# Calcular a média ponderada desses 3 números, utilizando os pesos de 20%, 30% e 50%

def calcululate_average(num1, num2, num3):
    average = (num1 + num2 + num3)/3
    weighted_average = ((num1 * 0.2) + (num1 * 0.3) + (num1 * 0.5))/3
    return average, weighted_average

numero1 = int(input("Digite o primeiro Numero"))
numero2 = int(input("Digite o segundo Numero"))
numero3 = int(input("Digite o terceiro Numero"))

media, media_ponderada = calcululate_average(numero1, numero2, numero3)
print(media)
print(media_ponderada)
