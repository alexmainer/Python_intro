years = int(input("Input Year: "))
if years % 4 == 0 % 400 == 0 and years % 100 != 0:
    print("This is a leap year")
else:
    print("This is not a leap year")
