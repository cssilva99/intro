# Calcule o valor do imposto a ser pago sobre o salário anual
# Pedir entrada de dados do utilizador

salario = float(input("Digite por favor o seu salário :"))

if salario <= 15000:
    print("Irá pagar  ".join(0,2*salario))
else :
    print("Irá pagar ".join(0,3*salario))