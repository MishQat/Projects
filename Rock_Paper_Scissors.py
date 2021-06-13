import random,sys

rpc_list = ["Rock", "paper", "Scissors"]

rpc_random = random.choice(rpc_list)

try:
    user_input= str(input("Rock, Paper or Scissors?. If you wish to quit. type Quit: "))
except:
    print("invalid input")

def rpc():
    if rpc_random == "Rock" and user_input == "Paper":
        print("Computer picked Rock ")
        print("User wins!")
        
    elif rpc_random == "Rock" and user_input == "Scissors":
        print("Computer picked Rock")
        print("Computer wins!")
    
    elif rpc_random == "Paper" and user_input == "Rock":
        print("Computer picked Paper")
        print("Computer wins!")
    elif rpc_random == "Paper" and user_input == "Scissors":
        print("Computer picked Paper")
        print("User wins!")
    elif rpc_random == "Scissors" and user_input == "Rock":
        print("Computer picked Scissors")
        print("User wins!")

    elif rpc_random == "Scissors" and user_input == "Paper":
        print("Computer picked Scissors")
        print("Computer wins!")

    elif rpc == user_input:
        print("Draw. well played")
    elif user_input=="Quit":
        sys.exit()
    else:
        print("your input was invalid")
    
        

rpc()
