"""{
input("Enter Your Name:")

input("Enter Your Age:")

# The input() function is used to take input from the user. It always returns a string.

name = input("Enter your name:")
print("Welcome", name)
print(type(name))


# we can use the str() function also but it is not necessary as the input() function already returns a string.

name = str(input("Enter your name:"))
print("Welcome", name)
print(type(name))

x = input("Enter your age:") # input function always returns a string
print("Your age is : ", x)
print(type(x)) 


# To convert the input to an integer, we can use the int() function

age = int(input("Enter your age:"))
print("Your age is : ", age)
print(type(age))

# To convert the input to a float, we can use the float() function

salary = float(input("Enter your salary:"))
print("Your salary is:", salary)
print(type(salary))


name = str(input("Enter your name:"))
print("Welcome", name)
print(type(name))
}"""

name = input("Enter your name: ")
Grade = int(input("Enter your grade: "))
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))

print("Welcome",name, "Your grade is", Grade, "Your age is", age, "Your salary is", salary)
print(type(name), type(Grade), type(age), type(salary))