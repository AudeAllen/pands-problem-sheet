# collatz.py 
# This program just asks the user to input any
# positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one. 

# Author: Audrey Allen

# Function below is the collatz function which performs the calculation as specified in the opening comments
# positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

def collatz(n):
    while n > 1:
        print(n, end=' ')
        if (n % 2):
            # n is odd
            n = 3*n + 1
        else:
            # n is even
            n = n//2

    print(1, end='')

#Some error handing below - While true checking if the input is an integer
#The input has to be an integer and has to be a positive number
#If the user inputs a negative number or a string the program throws a warning message back to the user 

while True:
    try:
        n = int(input('Please enter a positive integer: '))
        if n < 0: 
            print ("Enter only positive numbers\n")       
            continue
        elif n > 0:
            print ("This number is ok as it is a postive integer\n")
            print('collatz Sequence: ', end='')
            collatz(n) 
            break        
    except ValueError as e:
        print ("Must be an integer- Go again!!!!!!")            
        continue
    break

    
