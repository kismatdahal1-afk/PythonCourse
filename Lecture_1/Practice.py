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
"""{ <class 'int'>
     <class 'str'>
     <class 'float'>
     <class 'bool'>
     <class 'list'>
}"""


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


# Q11: Determine the output of the following expressions:
#      - 10 + 5 * 2
#      - (10 + 5) * 2
#      - 20 / 4 + 3
#      - 100 // 3
#      - 100 % 3


# Q12: Write a program to swap the values of two variables
#      a = 10, b = 20
#      After swap: a = 20, b = 10


# Q13: Test the following comparison operators and print results:
#      - 15 > 10
#      - 15 == 15
#      - 20 < 10
#      - 10 != 5
#      - 10 >= 10


# Q14: Test the following logical operators:
#      - True and False
#      - True or False
#      - not True
#      - (10 > 5) and (20 > 15)


# ============================================================================
# 5. DATA TYPE CONVERSION
# ============================================================================

# Q15: Convert the following:
#      - Convert "123" to integer
#      - Convert 456 to string
#      - Convert "3.14" to float
#      - Convert 1 to boolean
#      - Convert 0 to boolean


# Q16: Create a program that:
#      - Takes a string "100"
#      - Converts it to integer
#      - Adds 50 to it
#      - Prints the result


# Q17: What will be the output? Predict first, then verify:
#      - str(100)
#      - int("50") + int("30")
#      - float("2.5") * 2
#      - int(3.9)
#      - int(3.1)


# Q18: Convert temperature from Celsius to Fahrenheit
#      Formula: F = (C * 9/5) + 32
#      Given C = 25, find F and ensure proper conversion


# ============================================================================
# 6. USER INPUT
# ============================================================================

# Q19: Write a program to:
#      - Ask user for their name
#      - Ask user for their age
#      - Print a greeting message using their input


# Q20: Write a program to take two numbers as input from user and print their sum


# Q21: Create a simple calculator that:
#      - Takes two numbers as input
#      - Takes an operator as input (+, -, *, /)
#      - Performs the operation and prints the result


# Q22: Write a program that:
#      - Asks user for length and width of a rectangle
#      - Calculates and prints the area


# Q23: Take the user's name and age as input
#      Calculate the birth year (assume current year is 2024)
#      Print a message: "Hi [name], you were born around [birth_year]"


# ============================================================================
# 7. MIXED PROBLEMS (Combining Multiple Concepts)
# ============================================================================

# Q24: Create a program for a simple shopping cart:
#      - Ask user for number of items
#      - Ask for price of each item
#      - Calculate total
#      - Apply a 10% discount if total > 500
#      - Print the final bill


# Q25: Write a program that:
#      - Takes a student's marks in 3 subjects as input
#      - Calculates total and average
#      - Prints the results with proper formatting


# Q26: Create a program to:
#      - Ask user for principal amount, rate, and time
#      - Calculate simple interest using formula: SI = (P * R * T) / 100
#      - Print the result


# Q27: Write a program to find:
#      - The largest among three numbers entered by user
#      - The smallest among three numbers


# Q28: Create a program that:
#      - Asks for radius of a circle
#      - Calculates area and circumference
#      - Area = π * r²
#      - Circumference = 2 * π * r
#      - Print both results


# ============================================================================
# SOLUTIONS SECTION (Add your answers below)
# ============================================================================

# Start writing your solutions here...
