#Variables in Python
name = "Kismat"
age = 25
height = 5.8


#You can print the value of a variable using the print() function

print("My name is", name)
print("My age is", age)
print("My height is", height)

#You can also assign the value of one variable to another variable

name2 = name
print("My name is", name2)

#To find the datatype of a variable
#You can use the type() function to find the datatype of a variable
#The type() function returns the datatype of the variable as a string

#For example, if the variable is a string, the type() function will return "str"
#If the variable is an integer, the type() function will return "int"
#If the variable is a float, the type() function will return "float"

#Datatypes like, str, int, float, bool, list, tuple, set, dict, etc.

print(type(name))
print(type(age))
print(type(height))

#You can also use the type() function to find the datatype of a variable that has not been assigned a value yet

kisu = "HI"
a = True
b = None
print(type(kisu))
print(type(a))
print(type(b))

#Some keywords in Python that are used to define variables are: 
# False     None      True      and
# as        assert    async     await
# break     class     continue  def
# del       elif      else      except
# finally   for       from      global
# if        import    in        is
# lambda    nonlocal  not       or
# pass      raise     return    try
# while     with      yield
