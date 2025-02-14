# Missão 1: Restaurando as Regras Escolares 📝 
# O vírus apagou os critérios de aprovação dos alunos! Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

import time
nota_aluno = float(input("Informe a nota do aluno de 0 a 10: "))
if nota_aluno >= 6:
    print("Parabéns! Você foi APROVADO com a nota: ", nota_aluno)
elif nota_aluno <= 5:
    print("Sua nota ", nota_aluno,
          " foi a baixo da média. REPROVADO")
else:
    print("Nota inválida!")