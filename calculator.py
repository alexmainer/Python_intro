num1 = int(input("First number : "))
num2 = int(input("Second number : "))
calc = str(input("Enter Calculation : "))
if calc == '+':
    print(num1 + num2)
elif calc == '-':
    print(num1 - num2)
elif calc == '*':
    print(num1 * num2)
elif calc == '/':
    print(num1 / num2)
else:
    print("SYNTAX ERROR")