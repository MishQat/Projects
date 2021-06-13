import random,sys
head_tails = ("Heads", "Tails")

randz=random.choice(head_tails)

while True:
    try:
        User_input = input("Heads or Tails?. Press y to start and n to exit ")

    except:
        print("invalid input")
        sys.exit()
    if User_input =="y":
        print("The toss result were: " + randz)
        User_input_1= input("want to try again? press a ")
        if User_input_1 == "a":
            continue
        else:
            break
    else:
        print("chdoda khaw")
        break
