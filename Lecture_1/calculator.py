# simple calculator


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

    
#wap a program to input 2 floating numbers & print their average.

a = float(input("Enter a number: "))
b = float(input("Enter a number: "))

average = ((a + b)/2)

print("The average of given two numbers is: ", average)


#wap a program to input 2 numbers & print the result of their comparison (greater than, less than, equal to)
x = int(input("Enter first number: "))
y = int(input("Enter second numbe: "))

m = x>=y
n = x<=y

print(m)
print( n)




# WAP to calculate the volume of a solid havinf the combination of hemisphere and a cone having same radius.

r = float(input("Enter the radius of cone or hemisphere: "))
h = float(input("Enter the height of cone: "))

volume = (1/3 * 3.14 * r ** 2 *(2*r + h))

print("THe volume od the solid is: ", volume)
