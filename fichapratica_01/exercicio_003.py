salario = float(input("Digite por favor o seu salário :"))

if salario <= 15000:
    print("Irá pagar  ".join(0,2*salario))
elif salario <= 20000:
    print("Irá pagar ".join(0,3*salario))
elif salario <= 25000 :
    print("Irá pagar ".join(0,35*salario))
else:
    print("Irá pagar : ".join(0,4*salario))