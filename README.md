**Pands-Problem-Sheet Assignment** <br /> 
<br /> 
***Pands-Problem-Sheet contains all the assignments in the Higher Diploma in Data Analytics course*** <br /> 
***Here I will explain how I came to the solution of given tasks, reference the sources I researched for solving the problems and list the technologies I used for creating and testing the code*** <br />
<br />
<br />

# Table of contents
* [Weekly tasks](#weekly-tasks)
    * [helloworld](#helloworld)
    * [Accounts](#accounts)
    * [AccountsExtra](#accountsextra)
    * [Collatz](#collatz)
    * [Weekday](#weekday)


  


Weekly tasks
======
### ***helloworld***

  
1.The helloworld python program should  display Hello World! when it is run - This is week01 Task <br /> 
<br />
<br />
2. The Bank python program is a basic python program that adds two input variables in cent and outputs the result in euros and cents -<br /> 
   This program just reads in two money amounts and adds them together <br />
   The answer must be in readable format with a euro sign and decimal point between the euro and cent of the amount    <br />
   <details>
           <summary>Details of Input and Output</summary>
           <p>
   <br />
   <br />
   amount1 = int(input('Enter amount1(in cent):')) = 1566 - User must enter an integer    <br /> 
   <br />
   amount2 = int(input('Enter amount2(in cent):')) 23 - User must enter an integer    <br />
   <br />
   Then set up a new variable to calculate the amount in cents <br />
   <br />
   Then print the output <br />
   <br />
   print (f' The sum of  of {amount1} and {amount2}  is €{amountAsFormattedString}') = €15.89 <br />
</p>
</details>
<br />
<br />

### ***Accounts***          
             
3.1 The Accounts python program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).  <br />
This is the first part of week 03 task  <br />
  <details>
           <summary>Details of Input and Output</summary>
 </p> 
 The below piece of code checks firstly is the input a digit - While loop checks if not a digit program returns a message 'Enter only Numbers'<br /> 
 <br /> 
 Elif checks if the input is 10 characters in length <br /> 
 <br /> 
 If not program display message 'Account number must be 10 digits  <br /> 
 <br />
 <br />
 The below piece of code loops around until a valid number is input
 
while True:<br />
    number = input("Please enter your 10 digit account number:")<br />
    if not number.isdigit(): # check if a string contains a number with .isdigit()<br />
        print ("Enter only numbers\n")<br />
        continue<br />
    elif len(number) != 10:<br />
        print ("Account number must be 10 digits\n")<br />
        continue<br />
    else: <br />
        break<br />
 <br />
 <br />
 </p>
</details>
<br />
<br />

### ***AccountsExtra***   

3.2 The AccountsExtra python program reads in an account number of any length and outputs the account number with only the last 4 digits showing and the first part of the number replaced with X's  <br />
This is the second part of week 03 task  <br />
The difference between part 1 and part 2 of week 03 task is the second python program can read in an account number of ANY length
<br />
<br />
In regards to Week03 assignments I referenced stackoverflow website to assist with the task   <br />
<details>
           <summary>Details of Input and Output</summary>
 </p> 
 
 The below piece of code checks firstly is the input a digit - If not a digit program returns a message 'Enter only Numbers'<br />
 while True:  - Keep looping through until the user enters a number - Not checking length of number as in part 1 of the task <br />
    number = input("Please enter your account number:")<br />
    if not number.isdigit(): # check if a string contains a number with .isdigit()<br />
        print ("Enter only numbers\n")<br />
        continue<br />
    else: <br />
        break<br />
credit = (number)

Once the input is validated as being correct -  A digit must be entered
Only the last 4 digits of the number will appear - whatever the length of the input only the last 4 numbers will appear - The others will be masked as X's<br />
<br />
s = credit[-4:].rjust(len(credit), 'X')<br />
<br /> 
Print the new variable which is (s)<br /> 
<br /> 
print(s)<br /> 
<br />
<br />
</p>
</details>
<br />
<br />

### ***Collatz*** 

4. The Collatz python program  asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, 
but if it is odd, multiply it by three and add one.
Have the program end if the current value is one. <br />
 <details>
           <summary>Details of Input and Output</summary>
 </p> 
<br />
User is asked to enter a positive number/integer - 
<br />
<br />
Whilst number > 1 continue <br />
<br />
If number is not divisable by 2 then it is odd - Multiply by 3 and add 1 <br />
If number is divisable by 2 then it is even so then the program will divide by 2<br />
This loop will continue until the value is 1 then the program ends<br />
<br />
</p>
</details>
<br />
<br />

### ***Weekday*** 


5. The Weekday python program output whether today (the day from today's date) is a weekday or a weeknd day - If the days are 1-5 then is displays Yes, unfortunately today is a weekday - Otherwise the program displays It is the weekend, yay! <br />
Main reference for my work for this task was th website www.geeksforgeeks.org and also www.w3schools.com <br />
<br />
<details>
           <summary>Details of Input and Output</summary>
</p> 

<br />
<br />

Import datetime function to get todays day <br />

Setting today as the daynumber - Monday is 1, Tuesday is 2 etc <br />

dayno = datetime.datetime.today().weekday()<br />
<br />
<br />
if dayno < 5:<br />
    print ("Yes, unfortunately today is a weekday")<br />
else:  # 5 Sat, 6 Sun<br />
    print ("It is the weekend, yay!")<br />
</p>
</details>
<br />
<br />
6. The Function python progam takes the input from the user which is a positive floating-point number as input and outputs an approximation of its square root. The method that is to be used is the newton method. Newton's method works by taking an estimate of the root of the equation and calculating a more accurate estimate, a process that can be repeated to approximate the true value of the root more precisely. Main reference for my work for this task was th website www.geeksforgeeks.org and also www.w3schools.com
