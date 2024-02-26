# Boolean Operators

# Is 4 less than or equal to 4? <=
# result=(4 <= 4)
# print(result)

# Is 6 greater than 2? >
# result =(6 > 10)
# print(result)

# Is 5 greater than or equal to 6? >=
# result=( 5 >= 6)
# print(result)

# Is 5 equal to 5? ==
# print(5 == 7)

# Shortcut operators

# Addition 
# val = 8
# val = val + 3
# val += 3
# print(val)

# Subtraction 
# var = 20
# var -= 5
# print(var)


# Multiplication
# var = 5
# var *= 5
# print(var)


# num = 5
# num -= 2

# print(num)

# Are we the same object? is

# fname = 'Taylor'
# new_name = fname
# print(fname is new_name)

# in (a keyword)

# print('J' in 'January') #result is true
# print('F' in 'March') #result is false

# eval

# is_open = 'True'
# weekday = 'False'

# print(eval(is_open)) #eval evaluates the boolean nature of the code Eval let's you change it to a boolean.

# print(eval(weekday))

user_input = input('enter True or False')
print(type(user_input))
eval_result = eval(user_input)
print(type(eval_result))