Input = input("Enter of what you want to check panildrome of: ")
r_input=Input[::-1]#reversed the string(main logic)
if r_input == Input:
    print("Its a Panildrome")
else:
    print("Not a panildrome")
