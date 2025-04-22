# Verificador de números primos
# Crie um programa que peça ao utilizador para inserir um número e verificar se ele é primo



flag = True

for i in range(3):
    num = int(input("Insira um número primo: "))

    if num != 2 and num % 2 == 0 :
        flag = False
    elif num!= 3 and num % 3 == 0 :
        flag = False
    elif num!= 4 and num % 4 == 0 :
        flag = False
    elif num!= 5 and num % 5 == 0 :
        flag = False
    elif num!= 6 and num % 6 == 0 :
        flag = False
    elif num!=7 and num % 7 == 0 :
        flag = False
    elif num!= 8 and num % 8 == 0:
        flag = False
    elif num!= 9 and num % 9 == 0:
        flag = False
    else:
        flag = True
    if flag == True:
        print("Parabéns, o número é primo.")
    else:
        print("O número não é primo")