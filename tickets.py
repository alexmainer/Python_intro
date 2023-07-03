movie = str(input("Select Movie : "))
age = int(input("State your age please : "))
if age >= 18:
    print("3000")
elif 17 >= age >= 15:
    print("1500")
elif 14 >= age >= 12:
    print("1000")
elif 11 >= age >= 5:
    print("500")
elif age <=4:
    print("Free")
else:
    print("n/a")