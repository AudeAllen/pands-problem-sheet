#This program outputs whether or not today is a weekday. 


#Author: Audrey Allen


#Import datetime function

import datetime

# Seting today as the daynumber - Monday is 1, Tuesday is 2 etc

dayno = datetime.datetime.today().weekday()

if dayno < 5:
    print ("Yes, unfortunately today is a weekday")
else:  # 5 Sat, 6 Sun
    print ("It is the weekend, yay!")