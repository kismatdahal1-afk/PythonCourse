# Practice conditional statements in Python

#Q1. Wap to find the even or odd number entered by the user.

num = float(input("Enter a number: "))

if(num % 2 == 0):

    print(num, "is an even number.")

else:

    print(num, "is an odd number.")    


#Q2. Wap to find the greatest number among three numbers entered by the user.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if(a > b > c):
    print(a, "is the greatest number among the three numbers.")
elif(b > a > c):
    print(b, "is the greatest number among the three numbers.")
else:
    print(c, "is the greatest number among the three numbers.")    

    


#Q3. Wap to find whether the number entered by the user is a multiple of 7 or not.

num = float(input("Enter a number: "))

if(num % 7 == 0):

    print(num, "is multiple of 7.")

else:

    print(num, "is not multiple of 7.")    

    