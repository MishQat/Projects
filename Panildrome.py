Input = input("Enter of what you want to check panildrome of: ")
r_input=Input[::-1]
if r_input == Input:
    print("Its a Panildrome")
else:
    print("Not a panildrome")
