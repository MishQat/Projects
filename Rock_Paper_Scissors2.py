import random,sys


rpc_list = ["Rock", "paper", "Scissors"]

rpc_random = random.choice(rpc_list)

try:
    user_input= str(input("Rock, Paper or Scissors? Or (q)uit: "))
except:
    print("invalid input")

def rpc():
    while True:
        if user_input == "q":
            print("Quitting...")
            sys.exit()
        elif rpc_random == "Rock" and user_input == "Paper":
            print(rpc_random)
            print("User won!")
            break
        elif rpc_random =="Rock" and user_input == "Scissors":
            print(rpc_random)
            print("Computer won!")
            break
        elif rpc_random == "Paper" and user_input == "Rock":
            print(rpc_random)
            print("Computer won!")
            break
        elif rpc_random == "Paper" and user_input == "Scissors":
            print(rpc_random)
            print("User won!")
            break

        elif rpc_random =="Scissors" and user_input == "Rock":
            print(rpc_random)
            print("User won!")
            break
        elif rpc_random == "Scissors" and user_input == "Paper":
            print(rpc_random)
            print("Computer won!")
            break
        elif rpc_random == user_input:
            print("Draw")
            break
        else:

             user_input_1=input("Your input is invalid want to try again?yes/no ")
             if user_input_1 == "yes":
                 continue
             else:
                sys.exit()
rpc()
