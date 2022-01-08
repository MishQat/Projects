import random,sys
User_wins = 0
User_looses = 0
User_ties = 0
rpc_ = ["rock", "paper", "scissors"]
while True:#main loop
    random.shuffle(rpc_)#shuffler
    rpc_random = random.choice(rpc_)#randomiser
    print(f"wins {User_wins}, looses {User_looses}, ties {User_ties}")
    while True:
        user_input = str(input("rock, paper or scissors, press (q)uit to quit... "))
        user_input = user_input.lower()
        if user_input == "q":
            sys.exit()#exits if user dosent wants to play
        if user_input =="rock" or user_input == "paper" or user_input == "scissors":
            break#user picks what he wants to play
        else:
            print("invalid input try again... ")#for invalid input
            continue
    #main thing that makes the game work   
    #main logic
    if user_input == rpc_random:
        print(f"Computer played {rpc_random}")
        print("Draw!")
        User_ties = User_ties + 1
    elif user_input == "rock" and rpc_random == "paper":
        print(f"Computer played {rpc_random}")
        print("User won!")
        User_wins = User_wins + 1
    elif user_input =="rock" and rpc_random == "scissors":
        print(f"Computer played {rpc_random}")
        print("Computer won!")
        User_looses = User_looses +1
    elif user_input == "paper" and rpc_random == "rock":
        print(f"Computer played {rpc_random}")
        print("Computer won!")
        User_looses = User_looses + 1
    elif user_input == "paper" and rpc_random == "scissors":
        print(f"Computer played {rpc_random}")
        print("User won!")
        User_wins = User_wins +1
    elif user_input =="scissors" and rpc_random == "rock":
        print(f"Computer played {rpc_random}")
        print("User won!")
        User_wins = User_wins+1
    elif user_input == "scissors" and rpc_random == "paper":
        print(f"Computer played {rpc_random}")
        print("Computer won!")
        User_looses = User_looses+1
