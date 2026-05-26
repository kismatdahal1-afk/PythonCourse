# Python Basics Practice Questions
# Topics: Printing, Variables, Data Types, Identifiers, Keywords, Operators, Type Conversion, Input

# ============================================================================
# 1. PRINTING QUESTIONS
# ============================================================================

# Q1: Print the following text: "Hello, Python!"
# Expected Output: Hello, Python!

#Ans
print("Hello, pyhon!")

# Q2: Print three lines using a single print statement with newline characters
# Expected Output:
# Line 1
# Line 2
# Line 3

#Ans
print("Line1\nLine2\nLine3")


# Q3: Print a sentence with multiple variables using concatenation
# Example: name = "Kismat", age = 17
# Expected Output: Kismat is 17 years young

#Ans
name = "Kismat"
age = "17"
print(name, "is", age,"years young")

# ============================================================================
# 2. VARIABLES AND DATA TYPES
# ============================================================================

# Q4: Create three variables to store:
#     - Your name (string)
#     - Your age (integer)
#     - Your height in meters (float)
# Then print all three values

#Ans
name = "Kismat"
age = "17"
height = "5.8"

print("name: ",name)
print("age: ", age)
print("height: ", height)


# Q5: Find the data type of the following values:
#     - 42
#     - "Python"
#     - 3.14
#     - True
#     - [1, 2, 3]

#Ans
num1 = 42
num2 = "Python"
num3 = 3.14
num4 =  True
num5 = [1, 2, 3]

print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))
print(type(num5))

#Output
    #<class 'int'>
    # <class 'str'>
    # <class 'float'>
    # <class 'bool'>
    #<class 'list'>


# Q6: Create a variable with the value 100 and check its type using type()

#Ans

var1 = 100
print(type(var1))

#Output:   <class 'int'>



# Q7: Write a program that stores the cost of 3 items and calculates the total
#     Item1: 50, Item2: 75, Item3: 100

item1 = 50
item2 = 75
item3 = 100

total = (item1 + item2 + item3)
print("The total items is: ", total)

#Output:    The total items is:  225


# ============================================================================
# 3. IDENTIFIERS AND NAMING RULES
# ============================================================================

# Q8: Which of the following are valid identifiers? Explain why or why not:

#ANS

#     - my_variable            ✅ Valid
#     - 2nd_number             ❌ Invalid	Cannot start with a number (starts with '2')
#     - _private_var           ✅ Valid
#     - my-variable            ❌ Invalid	Hyphen (-) is not allowed (Python interprets as subtraction)
#     - MyVariable             ✅ Valid
#     - for                    ❌ Invalid	Reserved keyword in Python (used for loops)
#     - student_name           ✅ Valid 


# Q9: Create 5 variables with appropriate names for storing:
#     - Total amount of money
#     - Student's first and last name
#     - Number of students in a class
#     - Price per item
#     - Whether a light is on or off

#Ans
Tamount = 50000.25
Students_First_name =" Kismat"
Students_Last_Name = "Dahal"
Tstudents = 40
ppitems = 250
light = True #or
light = False #or
light = "on" 



# ============================================================================
# 4. OPERATORS
# ============================================================================

# Q10: Perform the following calculations:
#      - Add 25 and 15
#      - Subtract 50 from 100
#      - Multiply 12 by 8
#      - Divide 144 by 12
#      - Find remainder when 17 is divided by 5
#      - Calculate 2 raised to power 5

#Ans 
print(25+15)
print(100-50)
print(12*8)
print(144/12)
print(17%5)
print(2**5)  



# Q11: Determine the output of the following expressions:
#      - 10 + 5 * 2
#      - (10 + 5) * 2
#      - 20 / 4 + 3
#      - 100 // 3
#      - 100 % 3

#Ans
print(10 + 5 * 2) 
print((10 + 5) * 2)
print(20 / 4 + 3)
print(100 // 3)
print(100 % 3)
print(100 / 3)


# Q12: Write a program to swap the values of two variables
#      a = 10, b = 20
#      After swap: a = 20, b = 10

a = 10
b = 20

c = a   # Store original value of 'a' before swapping

a = b
b = c

print("After swap a= ", a, "b = ", b)


# Q13: Test the following comparison operators and print results:
#      - 15 > 10
#      - 15 == 15
#      - 20 < 10
#      - 10 != 5
#      - 10 >= 10

#Ans
print(15 > 10)   #True
print(15 == 15)  #True
print(20 < 10)   #False
print(10 != 5)   #True
print(10 >= 10)  #True


# Q14: Test the following logical operators:
#      - True and False
#      - True or False
#      - not True
#      - (10 > 5) and (20 > 15)

#Ans
print(True and False)
print(True or False)
print(not True)
print((10 > 5) and (20 > 15))

# ============================================================================
# 5. DATA TYPE CONVERSION
# ============================================================================

# Q15: Convert the following:
#      - Convert "123" to integer
#Ans
var1 = int("123")
print(type(var1))

#      - Convert 456 to string
#Ans
var2 = ("456")
print(type(var2))

#      - Convert "3.14" to float
#Ans
var3 = float("3.14")
print(type(var3))

#      - Convert 1 to boolean
#Ans
var4 = bool(1)
print(type(var4))
print("Output", var4)   #True

#      - Convert 0 to boolean
#Ans
var5 = bool(0)
print(type(var5))
print("Output", var5)  #False



# Q16: Create a program that:
#      - Takes a string "100"
#      - Converts it to integer
#      - Adds 50 to it
#      - Prints the result

#Ans
val1 = ("100")
val2 = int("100")

print("Result is: ", val2 + 50)


# Q17: What will be the output? Predict first, then verify:
#      - str(100)
#      - int("50") + int("30")
#      - float("2.5") * 2
#      - int(3.9)
#      - int(3.1)

#Ans
print(str(100))
print(int("50") + int("30"))
print(float("2.5") * 2)
print(int(3.9))
print(int(3.1))

# Q18: Convert temperature from Celsius to Fahrenheit
#      Formula: F = (C * 9/5) + 32
#      Given C = 25, find F and ensure proper conversion

#Ans
c = 25
print("25 degree celcius is equals to ", (c * 9/5) + 32, "Fahrenheit")


# ============================================================================
# 6. USER INPUT
# ============================================================================

# Q19: Write a program to:
#      - Ask user for their name
#      - Ask user for their age
#      - Print a greeting message using their input

#Ans
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Welcome ", name, "your age is", age)


# Q20: Write a program to take two numbers as input from user and print their sum

#Ans
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("The sum of given numbers is: ", x + y)


# Q21: Create a simple calculator that:
#      - Takes two numbers as input
#      - Takes an operator as input (+, -, *, /)
#      - Performs the operation and prints the result

#Ans

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("The sum of given numbers is: ", x + y)
print("The sub of given numbers is: ", x - y)
print("The product of given numbers is: ", x * y)
print("The quoitent of given numbers is: ", x / y)


# Q22: Write a program that:
#      - Asks user for length and width of a rectangle
#      - Calculates and prints the area

length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))

print("The area of rectangle is: ", length * width, "square unit")


# Q23: Take the user's name and age as input
#      Calculate the birth year (assume current year is 2026)
#      Print a message: "Hi [name], you were born around [birth_year]"

#Ans

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hi", name, "you were born around ", 2082 - (2001 + age))

# ============================================================================
# 7. MIXED PROBLEMS (Combining Multiple Concepts)
# ============================================================================

# Q24: Create a program for a simple shopping cart:
#      - Ask user for number of items
#      - Ask for price of each item
#      - Calculate total
#      - Apply a 10% discount if total > 500
#      - Print the final bill

#Ans

items = int(input("Enter no of items: "))

price = float(input("Enter the price of item: "))

total = items * price

discount = (total * (10/100))

final = total - discount

print("The final bill is:  ", final)


# Q25: Write a program that:
#      - Takes a student's marks in 3 subjects as input
#      - Calculates total and average
#      - Prints the results with proper formatting

#Ans

maths = float(input("Enter the marks obtained in maths: "))
computer = float(input("Enter the marks obtained in computer: "))
physics = float(input("Enter the marks obtained in physics: "))

total = maths + computer + physics
average = total/3

print("The total of the marks of three subjects is:", total, "and average is: ", average)


# Q26: Create a program to:
#      - Ask user for principal amount, rate, and time
#      - Calculate simple interest using formula: SI = (P * R * T) / 100
#      - Print the result

#Ans

p  = float(input("Enter the principal amount: "))
r  = float(input("Enter the rate: "))
t = float(input("Enter the time in years: "))

simple_interest = (p * t * r)/100

print("The simple interest is: ", simple_interest)


# Q27: Write a program to find:
#      - The largest among three numbers entered by user
#      - The smallest among three numbers

#Ans
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b > c:

    print("The largest number is: ", a)

elif b > a > c:

    print("The largest number is: ", b) 

else :

    print("The largest number is: ", c)



# Q28: Create a program that:
#      - Asks for radius of a circle
#      - Calculates area and circumference
#      - Area = π * r²
#      - Circumference = 2 * π * r
#      - Print both results

#Ans

r = float(input("Enter the radius of circle: "))

area = 3.14 * r**2
circumference = 2 * 3.14 * r

print("The area of circle is: ", area, "and circumference is: ", circumference)



