marks = int(input("Enter Students Score: "))
if 80 < marks <= 100:
    print("You Scored An 'A' ")
elif 60 < marks <= 80:
    print("You scored a 'B' ")
elif 40 < marks <= 60:
    print("You scored a 'C' ")
elif 20 < marks <= 40:
    print("You scored a 'D' ")
elif 0 < marks <= 20:
    print("You scored an 'E' ")
else:
    print("Wrong input")