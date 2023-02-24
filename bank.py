# bank.py 
# This program just reads in two money amounts and adds them together 
# The answer must be in readable format with a euro sign and decimal point between the euro and cent of the amount 
# Author: Audrey Allen

#Set up two input variables to read in amounts - amount1 and amount2

amount1 = int(input('Enter amount1(in cent):')) 
amount2 = int(input('Enter amount2(in cent):')) 

# New variable to calculate the new amount in euro and cents - money

money = int(amount1 + amount2)/100      #next you used format without printing, nor affecting value of "money"
amountAsFormattedString = '{:,.2f}'.format(money)

# Print Output

print (f' The sum of  of {amount1} and {amount2}  is €{amountAsFormattedString}') 






