#Conditional statements in Python
# In Python, we can use conditional statements to execute a block of code based on a certain condition. The most commonly used conditional statements in Python are if, elif, and else. 

age = 16

if(age>=18):
    print("You can vote.")
    print("You can drive.")
else:
    print("You cant vote.")
    print("You cant drive.")




#Wap to find the grade of a student based on the marks entered by the user.

sub = input("Enter the subject name: ")
marks = float(input("Enter your marks: "))

if(marks>27.25  and marks<=75):

    print("You have passed the ", sub, " exam with ", marks, " marks. Congratulations!" )

elif(marks==27.25):

    print("You have justpassed the ", sub, " exam with ", marks, " marks.: Need to improve." )    
 
elif(marks > 75):

    print("Error: Marks cannot be greater than 75. Please enter valid marks.")

else:

    print("You have failed the ", sub, " exam with ", marks, " marks. Talai goruu, paddainass mulaa" )    






#Wap to find the traffic light color and give the instruction to the driver.

light = input("Enter the color of traffic light: ")

if(light == "red"):
    
    print("Stop the vehicle.")

elif(light == "yellow"):

    print("Get ready for the veicle or look for the green light.")

else:

    print("Go and cross the road.")    





#Wap to find if a person can drive or not based on the age entered by the user.

age = int(input("Enter your age: "))

if(age>=18 and age<70):   # This and condition is used to check if the age is greater than or equal to 18 and less than 70. If both conditions are true then the block of code inside the if statement will be executed.
  
    print("You can drive.")
else:
    print("You cant drive.")    




#nested if statement
# In Python, we can also use nested if statements to check multiple conditions. A nested if statement is an if statement that is inside another if statement. The inner if statement will only be executed if the outer if statement is true.
if(age>=18):

    if(age<70):  # This if statement is nested inside the first if statement. It is used to check if the age is less than 70. If this condition is true then the block of code inside this if statement will be executed.

        print("You can drive.")
    else:
        print("You cant drive.")    
else:
    print("You cant drive.")        # This else statement is used to execute the block of code if the age is less than 18. If the age is less than 18 then the block of code inside this else statement will be executed.

    