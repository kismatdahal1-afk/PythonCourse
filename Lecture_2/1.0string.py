
# String operations in Python

str1 = "Hi its me Kismat"
str2 = 'I am learning Python'
str3 = """I am learning python and I am loving it"""

#but we can also use single quotes inside double quotes and vice versa
#eg

str = "I am learning python and I am loving it. It's great!"

#if we only use the single quotes multiple times in code then it will give an error as it will consider the first single quote as the end of the string and the second single quote as the start of the string and so on. 
# But if we use double quotes then it will consider the single quotes as part of the string and not as the end of the string.

str4 = print("HI guys its me Kismat.\n I am learning python and I am loving it.\n It's great!")

# Here we are using the escape character \n to print the string in multiple lines. The \n is used to create a new line in the string.



#concatenation of strings
# In Python, we can concatenate two or more strings using the + operator. The + operator is used to join two or more strings together.
str5 = "Hello guys "
str6 = "Welcome to Python programming"
str7 = str5 + str6
print(str7) 

 #Output: Hello guys Welcome to Python programming

 #length of a string
str8 = "Hi its me Kismat"
print(str8)                 #Output: Hi its me Kismat
print(len(str8))            #Output: 16

 # The len() function is used to find the length of a string. It returns the number of characters in the string including spaces.

print(len(str1 + str2 + str3  + str5 + str6 + str7 + str8))   #Output: 171


#indexing of a string
# In Python, we can access the characters of a string using indexing. The index starts from 0 for the first character, 1 for the second character and so on.
#  We can also use negative indexing to access the characters from the end of the string. The index -1 is used to access the last character, -2 for the second last character and so on.

val1 = "Hi its me Kismat"

char1 = val1[0]
print(char1)   #Output: H

char2 = val1[3]
print(char2)    #Output: i

char3 = val1[-1]
print(char3)    #Output: t

char4 = val1[-3]
print(char4)    #Output: m



#slicing of a string
# In Python, we can also access a range of characters in a string using slicing. The syntax for slicing is string[start:end] where start is the index of the first character and end is the index of the last character. The end index is not included in the slice.
#negative indexing is called slicing from the end of the string. The syntax for slicing from the end is string[-start:-end] where start is the index of the first character from the end and end is the index of the last character from the end. The end index is not included in the slice.

val2 = "Hi its me Kismat"
slice1 = val2[0:5]
print(slice1)   #Output: Hi its

str = "Apple"
str[-3:-1]   #Output: pl 


#string functions
# In Python, there are many built-in functions that we can use to manipulate strings. Some of the commonly used string functions are:


#the endswith() function is used to check if a string ends with a specific suffix. It returns True if the string ends with the specified suffix, otherwise it returns False.

str = "hi its me kismat"
print(str.endswith("mat")) #Output: True

print(str.endswith("me"))   #Output: False


#the capitalize() function is used to convert the first character of a string to uppercase and the rest of the characters to lowercase.
str = "hi its me kismat"

print(str.capitalize())  #Output: Hi its me kismat
print(str)              #Output: hi its me kismat

# The capitalize() function does not change the original string, it returns a new string with the first character capitalized and the rest of the characters in lowercase. If we want to change the original string, we can assign the result of the capitalize() function back to the original string variable.
str = str.capitalize()
print(str)           #Output: Hi its me kismat


# The replace() function is used to replace a specific substring with another substring in a string. It takes two arguments, the first argument is the substring to be replaced and the second argument is the substring to replace it with. The replace() function returns a new string with the specified substring replaced.

str = "hi its me kismat"
print(str.replace("kismat", "python"))  #Output: hi its me python
print(str)                              #Output: hi its me kismat

# The replace() function does not change the original string, it returns a new string with the specified substring replaced. If we want to change the original string, we can assign the result of the replace() function back to the original string variable.

print(str.replace("i", "s"))            #Output: hs sts me ksmat
print(str)                              #Output: hi its me kismat


# The find() function is used to find the index of the first occurrence of a specific substring in a string. It takes one argument, the substring to be found. The find() function returns the index of the first occurrence of the specified substring, or -1 if the substring is not found.
str = "hi its me kismat"
print(str.find("k"))     #Output: 10
print(str.find("hi"))    #Output: 0

print(str.find("xyz"))   #Output: -1

# The count() function is used to count the number of occurrences of a specific substring in a string. It takes one argument, the substring to be counted. The count() function returns the number of occurrences of the specified substring in the string.

str = "hi its me kismat"
print(str.count("i"))   #Output: 3
print(str.count("k"))   #Output: 1
print(str.count("z"))   #Output: 0