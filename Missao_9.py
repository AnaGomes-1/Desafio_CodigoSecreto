# Missão 9: Calculando Dobro de um Número 🛠️
# Os alunos precisam de um programa que ajude em cálculos rápidos. 
# Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
# ➡️ Exemplo: dobro(5)
# ➡️ Saída: "O dobro de 5 é 10"

num = int(input("Digite um número: "))

def dobro(dobrar_num):
    return dobrar_num * 2

print(f"O dobro de {num} é: {dobro(num)}")