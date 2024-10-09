import random
R



user_points = 0
computer_points = 0



options = ["R", "P", "T"] 
  
while True:
    user_points = input("R para escolher a pedra, /P para escolher papel, /T para escolher tesoura, ou Q para sair ").lower()

    if user_points = "q":
        break

    if user_points not in options:
        continue 


if user_points == computer_points:
    print("empate")

elif user_points == "p" and computer_points == "r": 
    user_points = user_points + 1 
    print("Ponto para você")

elif user_points == "t" and computer_points == "p": 
    user_points = user_points + 1 
    print("Ponto para você")

elif user_points == "r" and computer_points == "t": 
    user_points = user_points + 1 
    print("Ponto para você")

else: 
    computer_points = computer_points +1 
    print ("Você perdeu...")


