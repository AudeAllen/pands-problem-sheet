# es.py
# This python program reads in a text file (.txt) and outputs the number of  'e's' that are in the text file
# The filename is taken from an argument on the command line arg = sys.argv[1] - From the first argument so it ignores the name of the 
# Python program in the command line


#Import sys in order to pass an argument from the command line
#I am going to pass in two arguments here 1. is the name of the file and 2. is the letter that will be searched for

import sys
#First argument declared
arg = sys.argv[1]

#Second argument declared
letter = sys.argv[2]

# import os to check if file exists

import os
filename = arg 


#Continue with the below code while true

while True:  

#Check if Filename that was passed from command line exists

    if os.path.exists(arg): 


# explicit function to return the letter count
        def letterFrequency(arg, letter):
            # open file in read mode
            file = open(arg, "r")
        
            # store content of the file in a variable
            text = file.read()
        
            # declare count variable
            count = 0
        
            # iterate through each character
            for char in text:
        
                # compare each character with
                # the given letter
                if char == letter:
                    count += 1
        
            # return letter count
            return count
        
        
        # call function and display the letter count
        print(letterFrequency(arg, letter))
        
        #Exit out of routine
        
        break 
  
    else:  
        # User message if the file does not exist please create file or chose another filename to pass
                
        print (f' Filename: {arg} does not exist please create or chose another filename') 
        break

                             