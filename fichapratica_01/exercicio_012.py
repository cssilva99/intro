import sys

# Crie um menu com as opções
# 1. Criar
# 2. Atualizar
# 3. Eliminar
# 4. Sair

operacao = str(input("Digite um dos seguintes números correspondentes " \
"á operação que pretende realizar : \n"
"[1] - Criar \n" \
"[2] - Atualizar \n" \
"[3] - Eliminar \n" \
"[4] - Sair"
))

nome = ""
nif = 0

def registo_utilizador():
    nome = str(input("Digite o seu nome : "))
    nif = int(input("Digite o seu NIF: "))

def atualizacao_utilizador(verifica_nome):
    if nome == verifica_nome and nif == verifica_nif :
        nif = int(input("Digite o seu NIF: "))

def eliminar_utilizador():
    if nome == verifica_nome and nif == verifica_nif :
        nome = ""
        nif = 0
        

if operacao == "1" :
    registo_utilizador()
elif operacao == "2" :
    verifica_nome = str(input("Digite o seu nome : "))
    verifica_nif = int(input("Digite o seu NIF : "))
    atualizacao_utilizador(verifica_nome)
elif operacao == "3" :
    eliminar_utilizador()
elif operacao == "4" :
    sys.exit()