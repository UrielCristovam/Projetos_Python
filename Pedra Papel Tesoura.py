import random

Sua_Pontuação = 0
Pontuação_Computador = 0

opcoes = ["R","T","P"]
            
while True:
    Sua_Pontuação = input("escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair").lower()
    if Sua_Pontuação == 'q':
        break

    Pontuação_Computador = random.randint(0, 2)
    Opcao_computador = opcoes[Pontuação_Computador]

    print("O computador escolheu " + Opcao_computador)

    if Sua_Pontuação not in opcoes: 
        continue

if Sua_Pontuação == Pontuação_Computador:
    print("Empate")


elif Sua_Pontuação == "r" and Pontuação_Computador == "t":
    print ("Você ganhou!")
    Sua_Pontuação = Sua_Pontuação + 1

elif Sua_Pontuação == "p" and Pontuação_Computador == "r":
    print ("Você ganhou!")
    Sua_Pontuação = Sua_Pontuação + 1

elif Sua_Pontuação == "t" and Pontuação_Computador == "p":
    print ("Você ganhou!")
    Sua_Pontuação = Sua_Pontuação + 1

else:
    print("Voce perdeu")
    Pontuação_Computador = Pontuação_Computador + 1