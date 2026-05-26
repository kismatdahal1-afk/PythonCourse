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