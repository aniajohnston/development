''' Class 4 Strings '''

# String operators

'''Concatenation''' #adding our strings together. The plus operator.

first_name = 'Ania'
last_name = 'Johnston'

full_name = first_name +' '+last_name #creating a space use + ' ' +

print(full_name)

''' Multiplication '''

greeting = ' hip hip hooray'*3

print(greeting)



# Reference vs Value equality == vs is
x = 'hello'
str2 = 'HELLO'.lower() #string method

print(str2)

print(x==str2)

print(x is str2) #they are not exactly the same object.
print(id(x))
print(id(str2))

# even if str2 and x  both = 'hello' the is statement would be false.the == would be true though.

''' in - Returns True if a string appears inside another string (as a substring), and False otherwise.'''

test_character = 'b'
test_string = 'bananas'

print(test_character in test_string)

#test if a certain character is in a string

''' create a quick test to see if the sub string 'spreh' can be found in the string 'Incomprehensibilities' '''
test_chars = 'spreh'
test_word = 'Incomprehensibilities'

print(test_chars in test_word)




''' len() - Returns the length of a string, aka the number of characters in a string.'''

alphabet = 'abcdefghijklmnopqrstuvwxyz' #our argument

length_of_alphabet = len(alphabet) #this requires one parameter, so one argument is in the function
#Len has a parameter. Alphabet is the argument.

print(length_of_alphabet) #tells us the length of the alphabet

animal = 'horse'
length_of_animal = len(animal)
print(length_of_animal)
# String methods

word_1 = 'happy' #.capitalize

print(word_1.capitalize()) #apply as a variable or right to a string
print('happy'.capitalize())

ex_1 = 'cereal' # capitalize me!
print(ex_1.capitalize())
print('cereal'.capitalize())

word_2 = 'SuPrISe' # .casefold sanitizes and makes all cases the same. Cleans data. 
print(word_2.casefold())


ex_2 = 'RuMMaGe' # make me lower case!
print(ex_2.casefold())
print(ex_2.lower())

word_3 = 'ZOO'
print(word_3.casefold())
print(word_3.lower())


ex_3 = 'PLANET' # lets make this lower case?

print(ex_3.casefold())
print(ex_3.lower())


# isalnum() Are all my characters alphanumeric? Alphanumeric is A-Z, a-z and 0-9

test_1 = 'abcdef'
test_2 = '%$123'

print(test_1.isalnum())
print(test_2.isalnum())

ex_8 = '123*' 
print(ex_8.isalnum())

# isalpha() Are all characters in the string in the alphabet?

test_3 = 'abcde'
test_4 = '012345'

print(test_3.isalpha())
print(test_4.isalpha())



ex_9 = 'LMN0P' # Are we all in the alphabet

# isdecimal() Are all characters decimals? numerical. Would not identify sub or super scripts.

test_5 = '1234P'
test_6 = '234567'

print(test_5.isdecimal())
print(test_6.isdecimal())

ex_11 = '123456' # Check for decimals?

print(ex_11.isdecimal())

# isdigit() Are all characters digits? does the same thing. this supports decimals subscripts and superscripts.

test_7 = 'H1234'
test_8 = '9876'

ex_10 = '123Hello' # Check for digits!


# strip() Returns a trimmed version of the string
username = '   jessica123    '

username_clean = username.strip()
print(username)
print(username_clean)           #strip cleanses the spaces from the data
print(len(username))
print(len(username_clean)) #spaces can be characters too. len can be used for lists and dictionaries (key value pairs).

ex_21 = '  sportsfan876  ' # sanitize this string

'''
Write some code that will take a string from the user and print if it is a number or not.

Examples:
apple
False

4
True
'''

# Get input from user       #input function only converts all the input to a string.
user_input = input('Please enter your word ')

# print(user_input)
# print(type(user_input)) #type shows us data type.

# Test input
result = user_input.isdecimal()



# Provide output

        # print('Am I a number?',result) #the comma will automatically give you space.b

        # print(f'is {user_input} a number or not',result) #f is a formatted string in python.Curly brackets allow you to use your variables in the formatted string.

# Reference vs Value equality == vs is

x = 'hello'
str2 = 'HELLO'.lower() #we are applying the .lower() string method to that string

print(x)
print(str2)
print(x == str2)
print(x is str2)
print(id(x))
print(id(str2))
# the objects are not the same!

test_character = 'b'
test_string = 'bananas'
print(test_character in test_string)

word_1 = 'happy'
print(word_1.capitalize())

ex_1 = 'cereal' #capitalize me

print(ex_1.capitalize())
print('cereal'.capitalize())

word_2 = 'SuPrIsE' #make all lowercase
print(word_2.casefold())
print(word_2.casefold())

print('SurPriSe'.casefold())

word_4 = 'Good Evening'
print(word_4)
print(word_4.center(100)) #center takes one parameter the parameter we're using in this case is 100
print(word_4.center(50))

ex_4 = 'Hello world!'

print(ex_4.center(65))

word_5 = 'Pseudopseudohypoparthyroidism'
print(word_5.count('p')) #only counts lowercases

word_6 ='I\tam\ta\ttab'
print(word_6)
print(word_6.expandtabs(10))

create_new_line = 'I\t am\n a\n newline'
print(create_new_line)
print(word_6.expandtabs(15)) #this expands our tab even more.

#Find the position of the letter k

word_7 = 'Dichlorodiflouromethane'
print(word_7.find('f')) #if you're sure the letter is in there
print(word_7.index('f')) 

# print(word_7.index('x')) #breaks
print(word_7.find('x')) #produces -1

#Do both find and index incorporate 0?

# is alpha() are all characters in the string in the alphabet?

test_3 = 'abcde'
test_4 = '012345'
print(test_3.isalpha())
print(test_4.isalpha())

# islower() Lets check for lowercase needs all to be lowercase.

test_9 = 'Zebra'
test_10 = 'affordable'

print(test_9.islower())
print(test_10.islower()) 






















