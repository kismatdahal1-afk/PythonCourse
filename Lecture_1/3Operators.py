"""This is a simple Python program that demonstrates basic arithmetic operations such as addition,
 subtraction, multiplication, and division. The program calculates the sum, difference, product,
   and quotient of two pairs of numbers and prints the results to the console."""


# This program calculates the sum of two numbers and prints the result.

a = 5
b = 9
sum = a + b
print("The sum of the two numbers a & b is", sum)

#This programs calculates the difference of two numbers.

x = 10
y = 20
print("The Difference of the two numbers x & y is", x - y)

#This programs calculates the product of two numbers.

m = 15
n = 20
print("The Product of the two numbers m & n is", m * n)

#This programs calculates the quotient of two numbers.

i = 4000
j = 200
print("The Quotient of two numbers i & j is", i / j)


#This program demonstrates the use of various arithmetic operators in Python.

p = 10
k = 3

print(p+k) #Addition operator, it returns the sum of the two numbers. In this case, it returns the sum of 10 and 3, which is 13.
print(p-k) #Subtraction operator, it returns the difference of the two numbers. In this case, it returns the difference of 10 and 3, which is 7.
print(p*k) #Multiplication operator, it returns the product of the two numbers. In this case, it returns the product of 10 and 3, which is 30.
print(p/k) #Division operator, it returns the quotient of the division of the first number by the second number. In this case, it returns the quotient of 10 divided by 3, which is approximately 3.3333333333333335.
print(p%k) #Modulus operator, it returns the remainder of the division of the first number by the second number. In this case, it returns the remainder of 10 divided by 3, which is 1.
print(p**k) #Exponentiation operator, it raises the number to the power of the other number. In this case, it raises p to the power of k, which is 10 raised to the power of 3, resulting in 1000.

#Relational operators in Python

x = 10
y = 20

print(x > y) #Greater than operator, OUTPUT= False
print(x < y) #Less than operator, OUTPUT= True
print(x >= y) #Greater than or equal to operator, OUTPUT= False
print(x <= y) #Less than or equal to operator, OUTPUT= True
print(x == y) #Equal to operator, OUTPUT= False 
print(x != y) #Not equal to operator, OUTPUT= True


#Assignment operators in Python

num1 = 10
num2 = num1 + 15
print(num2)       #OUTPUT= 25

num2 += num1 #This is an assignment operator that adds the value of num1 to num2 and assigns the result back to num2. In this case, it adds 10 to 25 and assigns the result (35) back to num2.
print(num2)       #OUTPUT= 35

num2 -= num1 #This is an assignment operator that subtracts the value of num1 from num2 and assigns the result back to num2. In this case, it subtracts 10 from 35 and assigns the result (25) back to num2.
print(num2)       #OUTPUT= 25

num2 *= num1 #This is an assignment operator that multiplies num2 by num1 and assigns the result back to num2. In this case, it multiplies 25 by 10 and assigns the result (250) back to num2.
print(num2)       #OUTPUT= 250

num2 /= num1 #This is an assignment operator that divides num2 by num1 and assigns the result back to num2. In this case, it divides 250 by 10 and assigns the result (25) back to num2.
print(num2)       #OUTPUT= 25

num2 %= num1 #This is an assignment operator that calculates the modulus of num2 by num1 and assigns the result back to num2. In this case, it calculates 25 modulus 10, which is 5, and assigns that value back to num2.
print(num2)       #OUTPUT= 5

num2 **= num1 #This is an assignment operator that raises num2 to the power of num1 and assigns the result back to num2. In this case, it raises 5 to the power of 10, which is 9765625, and assigns that value back to num2.
print(num2)      #OUTPUT= 9765625

#Logical operators in Python
#Logical operators are used to combine conditional statements. The three logical operators in Python are and, or, and not.

a = 15
b = 20
print(not False)
print(not (a > b)) #This is a logical operator that negates the result of the comparison a > b. In this case, since a is not greater than b, the expression a > b evaluates to False. The not operator then negates this result, making the final output True.
print((a<b) and (b>a)) #This is a logical operator that combines two conditions using the and operator. In this case, the first condition (a < b) evaluates to True because 15 is less than 20, and the second condition (b > a) also evaluates to True because 20 is greater than 15. Since both conditions are True, the overall expression evaluates to True.
print((a<b) or (b>a)) #This is a logical operator that combines two conditions using the or operator. In this case, the first condition (a < b) evaluates to True because 15 is less than 20, and the second condition (b > a) also evaluates to True because 20 is greater than 15. Since at least one condition is True, the overall expression evaluates to True.



#Logical operators can also be used with boolean values. For example, if we have two boolean variables val1 and val2, we can use logical operators to combine their values.

val1 = True
val2 = False
print("and operator:", val1 and val2) #This is a logical operator that combines two boolean values using the and operator. In this case, val1 is True and val2 is False. Since the and operator requires both operands to be True for the result to be True, the overall expression evaluates to False.
print("or operator:", val1 or val2) #This is a logical operator that combines two boolean values using the or operator. In this case, val1 is True and val2 is False. Since the or operator requires at least one operand to be True for the result to be True, the overall expression evaluates to True
print("not operator:", not val1) #This is a logical operator that negates the value of a boolean variable. In this case, val1 is True, so the not operator negates it, making the final output False.
