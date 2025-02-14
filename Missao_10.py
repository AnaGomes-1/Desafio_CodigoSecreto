# Missão 10: Contando Letras 🔄
# O sistema precisa contar quantas letras há em um nome.
# ➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
# ➡️ Exemplo: contar_letras("Ana")
# ➡️ Saída:" O nome Ana tem 3 letras"

nome = input("Digite seu nome: ")

def contador_nome(nome):
    return len(nome)

qntd_letras = contador_nome(nome)
print("O nome ", nome, " tem ", qntd_letras, " letras!")