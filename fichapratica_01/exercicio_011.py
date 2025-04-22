# Programa que conta números em intervalos especifico
# Objectivo : Ler uma quantidade desconhecida de números inteiros positivos
# e contar quantos desses números estão em cada um dos seguintes intervalos :

# [0, 25]
# [26, 50]
# [51, 75]
# [76, 100]

# A entrada de dados termina quando um número negativo é inserido
# Contar quantos números estão em cada intervalo

num = 0

count_0_25 = 0
count_26_50 = 0
count_51_75 = 0
count_76_100 = 0

while num >= 0:
    num = int(input("Please input a number: "))
    if num <= 25:
        count_0_25 += 1
    elif num <= 50:
        count_26_50 += 1
    elif num <= 75 :
        count_51_75 += 1
    elif num <= 100 :
        count_76_100 += 1

print("count_0_25 is : " , count_0_25)
print("count_26_50 is : " , count_26_50)
print("count_51_75 is : " , count_51_75)
print("count_76_100 is : " , count_76_100)