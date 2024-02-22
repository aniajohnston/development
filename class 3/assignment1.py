'''This program calculates the perimeter of a triangle

Requirements
    - Comment your code
    +5
    - Assign meaningful variable names
    +5
    - Output a print statement, "The perimeter of your triangle is..." 
    +5
     - The test case for your program is side # 1 is 5, the base is 6, side # 2 is 10 
        +5
    - Output a print statement, "Is side 1 greater than side 2?" 
        +5
    - Output a print statement, "Is the base equal to side 1?"
        +5
    '''

'''The perimeter of a Triangle'''
'''Assignment 1'''
'''Ania Johnston'''
'''2-21-2024'''

# perimeter of triangle = side 1 + base + side 2

side_one = 5
base = 6
side_two = 10

perimeter = side_one + base + side_two
print('The perimeter of your triangle is...',perimeter)

greater = side_one > side_two
print('Is side 1 greater than side 2?',greater)

base = base == side_one
print('Is the base equal to side 1?', base)

