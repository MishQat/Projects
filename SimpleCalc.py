import sys
user_sum = 0 
user_sum = float(user_sum)#setting a sum value
while True:
    while True:#chekcs input for maths
        user_input=input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n(q)uit\nEnter what you want to do?... ")#asks user what to do
        if user_input == 'q':
            sys.exit()
        elif user_input == "1" or "2" or "3" or "4" or "5":
            break
    user_input_num1 = float(input("Enter your first number: "))
    user_input_num2 = float(input("Enter your second number: "))
    #Main math logic
    if user_input == "1":
        user_sum = user_input_num1 + user_input_num2
        print(f"Your Answer is {user_sum}")
    elif user_input == "2":
        user_sum = user_input_num1-user_input_num2 
        print(f"Your Answer is {user_sum}")
    elif user_input == "3":
        user_sum=user_input_num1 * user_input_num2
        print(f"Your Answer is {user_sum}")
    elif user_input =="4":
        user_sum = user_input_num1 / user_input_num2
        print(f"Your Answer is {user_sum}")
    elif user_input == "5":
        user_sum = user_input_num1 % user_input_num2
        print(f"Your Answer is {user_sum}")
