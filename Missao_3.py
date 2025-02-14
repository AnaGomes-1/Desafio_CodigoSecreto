# Missão 3: Recuperando o Sistema de Notas 📊
# As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F . Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:

#  - A (90-100) – "Parabéns, você tirou A!"
# - B (80-89) – "Muito bem, você tirou B."
# - C (70-79) – "Bom trabalho, você tirou C."
# - D (60-69) – "Fique atento, você tirou D."
# - F (menos de 60) – "Estude um pouco mais, você tirou F."

nota_aluno = int(input("Digite a nota do aluno: "))
if nota_aluno < 60:
    print("Estude um pouco mais, você tirou F.")
elif 60 <= nota_aluno <= 69:
    print("Fique atento, você tirou D.")
elif 70 <= nota_aluno <= 79:
    print("Bom trabalho, você tirou C.")
elif 80 <= nota_aluno <= 89:
    print("Muito bem, você tirou B.")
elif 90 <= nota_aluno <= 100:
    print("Parabéns, você tirou A!")
else:
    print("Nota Inválida!")