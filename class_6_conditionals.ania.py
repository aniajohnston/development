''' Conditionals '''

# x = 20
# y = 20
# if x > y:
#     print(f'{x} is greater than {y}') #you don't need the boolean
# elif y > x:
#     print(f'{y} is greater than {x}')
# else: # you don't evaluate on the else line
#     print(f'{x} and {y} are equal')

'''
Use the if and else keyword to create a program that will ask the user for 2 values. Have your program compare the two values and let the user know which value is bigger. (view word wrap)
'''

# # number_1 = int(input('Please enter a value:'))
# val_1 = int(input('Please input your number:'))
# val_2 = int(input('Please input your second number:'))
# print(val_1 , val_2)
# if val_1 > val_2:
#     print(f'Your first number {val_1} bigger')
# elif val_2 > val_1: #elif lets you evaluate additional conditions. You don't want to do an if over if over if because ___.
#     print(f'Your second number {val_2} bigger')
# else: 
#     print(f'Your numbers {val_1} and {val_2} are equal')


'''
Exercise

Write some code that prints “This is odd” if the user inputs an odd number.
(Hint: use an if statement)
Example:
User input: 7
This is odd

'''
# my_num = 11
# result = (my_num % 2)
# print(result)

# #remainder is 1 with odd and 0 with even.


# user_number = int(input('Type in a number:'))
# print(user_number) #print not in conditional is on left side.

# if user_number % 2 == 1:
#     print('This number is odd')


# We can use modulus to figure out odd or even
# val = 6
# result = val % 2
# print(result)


'''
Exercise
Add to your previous code so it prints “This is odd” if the user enters an odd number, and “This is even” if the user enters an even number.
(Hint: add an elif statement)

Examples:
User input: 7
This is odd

User input: 12
This is even

'''

user_number = int(input('Type in your number:'))
if user_number % 2 == 1:
    print('This number is odd')
else: #this tests for the other condition.
    print('This number is even')

#flow chat would look different