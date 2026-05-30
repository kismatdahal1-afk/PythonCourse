# Lists in Python
#each variable contains a single value, but sometimes we want to store multiple values in a single variable. In Python, we can use lists to store multiple values in a single variable. A list is a collection of items that are ordered and changeable. Lists are written with square brackets [] and the items are separated by commas.

marks1 = 25.2
marks2 = 30.5
marks3 = 28.7
marks4 = 65.2
marks5 = 66.5

#here we have 5 variables to store the marks of 5 students. Instead of using 5 variables, we can use a list to store all the marks in a single variable.

marks = [marks1, marks2, marks3, marks4, marks5]

#we can also directly create a list without using separate variables for each item.

marks = [25.2, 30.5, 28.7, 65.2, 66.5]

print(marks)        #Output: [25.2, 30.5, 28.7, 65.2, 66.5]
print(type(marks))  #Output: <class 'list'> 
print(len(marks))   #Output: 5
print(marks[0])     #Output: 25.2
print(marks[1])     #Output: 30.5
print(marks[2])     #Output: 28.7
print(marks[-1])    #Output: 66.5
print(marks[-3])    #Output: 28.7

# We can also store different types of data in a list. A list can contain items of different data types such as strings, integers, floats, etc.

students = ["Kismat", 65.25, 17, "Kapan"]
print(students)      #Output: ['Kismat', 65.25, 17, 'Kapan']
print(students[0])   #Output: Kismat
print(students[1])   #Output: 65.25


#List Slicing
marks = [55, 66, 77, 88, 99]
print(marks[0:4])    #Output: [55, 66, 77, 88]
print(marks[1:4])    #Output: [66, 77, 88] 
print(marks[2:])     #Output: [77, 88, 99]
print(marks[1:3])    #output: [66, 77]


#List Methods

list = [2 ,5 ,8, 9]
list.append(2)
list.sort()