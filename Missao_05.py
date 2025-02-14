# Missão 5: Recuperando o Cofre de Segurança 🔒
# O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha! Agora, apenas quem souber a combinação correta poderá acessá-lo.
# Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".

print("Vocë tem 3 tentativas para acertar a senha.")
acesso_cofre = "Python123"
for tentativa in range(3):
    senha = input("Digite a senha: ")
    if senha == acesso_cofre:
        print("Senha Correta")
        break
    else:
        tentativas_restantes = 2-tentativa
        if tentativas_restantes == 2:
            print("Senha incorreta! Você só tem mais ",
                  2-tentativa, " tentativas")
        elif tentativas_restantes == 1:
            print("Senha incorreta! Você só tem mais ",
                  2-tentativa, " tentativa")
        else:
            print("Suas tentativas acabaram e seu acesso ao cofre foi bloqueado.")