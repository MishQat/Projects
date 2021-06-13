Time = float(input("Enter hour: "))

Rate = float(input("Enter rate: "))

Payment = float(Time * Rate)

if Time is 40 or Time > 40:
    Payment = Payment * 1.5
    print(Payment)
else: 
    print(Payment)

