# Missão 2: O Sistema Eleitoral Secreto 📝 
# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

idade_aluno = int(input("Informe sua idade: "))
if idade_aluno >= 16:
    print("O aluno pode votar!")
else:
    print("Infelizmente você não esta apto a votar!")