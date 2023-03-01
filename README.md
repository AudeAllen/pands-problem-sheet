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
<br />
<br />

</p>
</details>

### ***Accounts***          
             
3.1 The Accounts python program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).  <br />
  <details>
           <summary>Details of Input and Output</summary>
 </p> 
 The below piece of code checks firstly is the input a digit - While loop checks if not a digit program returns a message 'Enter only Numbers'
 Elif checks if the input is 10 characters in length - If not program display message 'Account number must be 10 digits  <br /> 
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
3.2 The AccountsExtra python program reads in an account number of any length and outputs the account number with only the last 4 digits showing and the first part of the number replaced with X's   - This is week03 Task also <br />
<br />
<br />
In regards to Week03 assignments I referenced stackoverflow website to assist with the task   <br />
<br />
<br />
4. The Collatz python program  asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, 
but if it is odd, multiply it by three and add one.
Have the program end if the current value is one. <br />
<br />
<br />
5. The Weekday python program output whether today (the day from today's date) is a weekday or a weeknd day - If the days are 1-5 then is displays Yes, unfortunately today is a weekday - Otherwise the program displays It is the weekend, yay! <br />
<br />
<br />
6. The Function python progam takes the input from the user which is a positive floating-point number as input and outputs an approximation of its square root. The method that is to be used is the newton method. Newton's method works by taking an estimate of the root of the equation and calculating a more accurate estimate, a process that can be repeated to approximate the true value of the root more precisely. Main reference for my work for this task was th website www.geeksforgeeks.org and also www.w3schools.com
