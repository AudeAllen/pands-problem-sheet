# accounts.py 
# This program reads in an account number of any length and outputs the account number with only the last 4 digits showing
# and the first part of the number replaced with X's 
# Author: Audrey Allen


while True:
    number = input("Please enter your account number:")
    if not number.isdigit(): # check if a string contains a number with .isdigit()
        print ("Enter only numbers\n")
        continue
    else: 
        break


credit = (number)


s = credit[-4:].rjust(len(credit), 'X')
print(s)

 
print (f' Your Masked Account number is: {s}') 