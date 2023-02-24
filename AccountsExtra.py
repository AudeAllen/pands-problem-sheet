# accounts.py 
# This program reads in an account number of any length and outputs the account number with only the last 4 digits showing
# and the first part of the number replaced with X's 
# Author: Audrey Allen

# The below piece of code checks firstly is the input a digit - If not a digit program returns a message 'Enter only Numbers'

while True:
    number = input("Please enter your account number:")
    if not number.isdigit(): # check if a string contains a number with .isdigit()
        print ("Enter only numbers\n")
        continue
    else: 
        break


credit = (number)

# Once the input is validated as being correct -  A digit must be entered
# Only the last 4 digits of the number will appear - whatever the length of the input

s = credit[-4:].rjust(len(credit), 'X')
print(s)

 
print (f' Your Masked Account number is: {s}') 