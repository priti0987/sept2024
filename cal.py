#pythoncalculator :

operator = input("Enter an operator : (+ - * / ):")
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

if operator == "+":
    result = num1 +num1
elif operator == "-":
    result = num1-num2
elif operator == "*":
    result = num1*num2
elif operator == "/":
    result = num1/num2
else:
    print("Wrong operator  entered please start over again")

print(result)