''' Loops '''

''' While Loops '''


''' While my start value is less than my end value, we will increment by 1'''
# end = int(input('Please enter your number: ')) #input
# start = 0 #initialization
# while start < end: #condition
#     print(start) #just zero the first time
#     start += 1

#example: what will 25 do as our input?


''' While my start value is less than my end value, we will decrement by one - You can stop the infinite loop by hitting ctrl + c'''
# end = 20
# start = 0 #start is starting at zero, this is an infinite loop.
# while start < end:
#     print(start)
#     start -= 1



''' Example Create a while loop that prints every integer from 1 to 10.'''
start = 1
end = 11
while start < end:
    print(start)
    start += 1 #this operates on our start variable



'''
While Loops and User Input

While loops are often paired with user input. The condition for the loop might be what the user needs to enter to stop the loop. The user is prompted for input each time it loops, and something happens based on that input.
This allows you to take user input multiple times without writing multiple lines of input(). It also allows the user to control how much input they give.

Lets look at code that will run infinitely until the user tells it to "stop"
'''
# user_input = '' #initiating the string
# while user_input != 'stop': #entering the loop
#     user_input = input('Please input your code: ') #prompt the user
#     print(user_input)

# FOR LOOPS

#for loops iterate through a limited amount. only goes through iterable.
    
# last_name = 'Johnston'
# for l in last_name: #for item in collection
#     print(l)

# colors = ['purple', 'blue', 'orange', 'yellow']
# for c in colors:
#     print(c)



