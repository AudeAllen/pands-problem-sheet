# accounts.py 
# This program reads in a 10 character account number and outputs the account number with only the last 4 digits showing
# (and the first 6 digits replaced with Xs). 
# Author: Audrey Allen


while True:
    number = input("Please enter your 10 digit account number:")
    if not number.isdigit(): # check if a string contains a number with .isdigit()
        print ("Enter only numbers\n")
        continue
    elif len(number) != 10:
        print ("Account number must be 10 digits\n")
        continue
    else: 
        break



replacement = "XXXXXX"
MaskedAccountNumber = number.replace(number[0:6], replacement, 1)

print("Your Masked Account number is:  ", MaskedAccountNumber)  