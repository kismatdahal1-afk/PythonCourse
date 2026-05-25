num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
A = float(input("Type 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for modulus, 6 for exponentiation: "))
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
mod = num1 % num2
pow = num1 ** num2
for i in range(1, 7):
     if A == i:
        break
if A == 1:
    print("The sum of the two numbers is:", sum)
elif A == 2:
    print("The difference of two numbers is:", sub)
elif A == 3:
    print("The product of two numbers is:", mul)
elif A == 4:
    print("The quotient of two numbers is:", div)
elif A == 5:
    print("The remainder of two numbers is:", mod)
elif A == 6:
    print("The result of raising the first number to the power of the second number is:", pow)