# Leia três notas (de 0 a 20) e calcule a média ponderada.
# Diga se o aluno está aprovado (se tem uma nota maior que 9,5)

nota1 = float(input("Digite a primeira nota : "))
nota2 = float(input("Digite a segunda nota : "))
nota3 = float(input("Digite a terceira nota : "))

media_ponderada = (nota1*0,25) + (nota2*0,35) + (nota3*0,4)

if media_ponderada >= 9.5 :
    print("O aluno está aprovado")
else:
    print("O aluno não está aprovado")