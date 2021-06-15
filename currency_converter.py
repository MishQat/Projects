from py_currency_converter import convert
global str



def Currency_conv():
    print("User in 'EUR', 'BDT' format")
    user_input_1=str(input("welcome to Currency Converter!. Which currency do you want to convert from?: "))
    user_input_2 = int(input("How much you want to conver: "))
    user_input_3 = str(input("What you wanna convert to?: "))
    print(convert(base = user_input_1, amount = user_input_2, to = [f"{user_input_3}"]))



    
Currency_conv()
