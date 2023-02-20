# collatz.py 
# This program just asks the user to input any
# positive integer and outputs the successive values of the following calculation.
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, 
#but if it is odd, multiply it by three and add one.
#Have the program end if the current value is one. 

# Author: Audrey Allen


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
 
 
n = int(input('Enter positive number please: '))
print('collatz Sequence: ', end='')
collatz(n)