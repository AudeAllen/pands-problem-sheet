# bank.py 
# This program just reads in two money amounts and adds them together 
# The answer must be in readable format with a euro sign and decimal point between the euro and cent of the amount 
# Author: Audrey Allen

#Set up two input variables to read in amounts - amount1 and amount2
#Some error handling done to check that the user has input a positive number
#Mesesage appears to user if input is a string or is a negative number  



while True:
    try:
        # User prompted to enter amount 1
        amount1 = int(input('Enter amount1(in cent):'))
        if amount1 < 0: 
            # Check to see that it is a positive number that is entered
            print ("Enter only positive numbers\n")       
            continue
        elif amount1 > 0:
            # If user has entered a positive number then user is prompted to enter a second number

            print ("This number is ok as it is a postive integer\n")
            amount2 = int(input('Enter amount2(in cent):')) 
            
            # Sum of Amount1 and Amount2 / 100 to get the amount in euros and cent
            money = int(amount1 + amount2)/100  
            # Format the money variable to 2 decimal places    
            amountAsFormattedString = '{:,.2f}'.format(money)   

        
# Print Output
# Sum of Amount 1 an amount 2

        print (f' The sum of  of {amount1} and {amount2}  is €{amountAsFormattedString}')   
           
        break        
    except ValueError as e:
        # Message appears here if the user enters a string!!

        print ("Must be an integer- Go again!!!!!!")            
        continue
    break


