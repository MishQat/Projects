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
        elif user_input == "Rock" and rpc_random == "Paper":
            print(rpc_random)
            print("User won!")
            break
        elif user_input =="Rock" and rpc_random == "Scissors":
            print(rpc_random)
            print("Computer won!")
            break
        elif user_input == "Paper" and rpc_random == "Rock":
            print(rpc_random)
            print("Computer won!")
            break
        elif user_input == "Paper" and rpc_random == "Scissors":
            print(rpc_random)
            print("User won!")
            break

        elif user_input =="Scissors" and rpc_random == "Rock":
            print(rpc_random)
            print("User won!")
            break
        elif user_input == "Scissors" and rpc_random == "Paper":
            print(rpc_random)
            print("Computer won!")
            break
        elif user_input == rpc_random:
            print(rpc_random)
            print("Draw")
            break
        else:
            print("invalid input try again")
            sys.exit()        
rpc()
