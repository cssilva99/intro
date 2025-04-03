def calculus(num1, num2):
    sum = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    return sum, subtraction, multiplication, division

numero1 = int(input("Digite o primeiro Numero"))
numero2 = int(input("Digite o segundo Numero"))

sum, subtraction, multiplication, division = calculus(numero1, numero2)
print(sum)
print(subtraction)
print(multiplication)
print(division)