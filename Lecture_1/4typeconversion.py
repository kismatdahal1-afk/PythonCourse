# This program demonstrates type conversion in Python.
# In the below code, we have added an integer (a) and a float (b). The result is a float because Python automatically converts the integer to a float before performing the addition. This is known as implicit type conversion or type coercion.
a = 4
b = 2.45

sum = a + b
print("Sum is:", sum)  #OUTPUT= 6.45

# In the below code, we have explicitly converted the string "10" to a float using the float() function. This is known as explicit type conversion or type casting. After converting the string to a float, we can perform arithmetic operations with it.
# But python automatically converts the integer to a float before performing the addition. This is known as implicit type conversion or type coercion.

x = float("10")
y = 5

print(type(x))
print(type(y))
print("sum is:", x + y) #OUTPUT= 15.0


# In the below code, we have explicitly converted the string "10" to an integer using the int() function. This is known as explicit type conversion or type casting. After converting the string to an integer, we can perform arithmetic operations with it.
# But python automatically converts the integer to a float before performing the addition. This is known as implicit type conversion or type coercion.

x = int("10")
y = 5

print(type(x))
print(type(y))
print("sum is:", x + y)  #OUTPUT= 15

#practice of type conversion
m = "3.14"
n = 4

print(type(m))
print(type(n))
print("Product is:", float(m) + n)  #OUTPUT= 7.14