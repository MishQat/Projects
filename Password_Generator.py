import random, array
user_input_length = int(input('length of password?: '))
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<',"[", "]", "{", "}",";", "'", "\'" ]
random.shuffle(DIGITS)
random.shuffle(LOCASE_CHARACTERS)
random.shuffle(UPCASE_CHARACTERS)
random.shuffle(symbols)
combined_list = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS + symbols
rand_numb = random.choice(DIGITS)
rand_locar = random.choice(LOCASE_CHARACTERS)
rand_upcar = random.choice(UPCASE_CHARACTERS)
rand_symbols = random.choice(symbols)
rand_noshit = random.choice(rand_locar + rand_numb +rand_upcar + rand_symbols)
random.shuffle(rand_noshit)
rand_shit = rand_locar + rand_numb +rand_upcar + rand_symbols + rand_noshit
for x in range(user_input_length):
    rand_shit = rand_shit + random.choice(combined_list)
rand_shit = array.array("u",rand_shit)
password = random.shuffle(rand_shit)
password = ""
for x in rand_shit:
    password = password + x
print (f"Your personal password is {password} made just for you and only you :wink")
