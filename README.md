**Pands-Problem-Sheet Assignment** <br /> 
<br /> 
***Pands-Problem-Sheet contains all the assignments in the Higher Diploma in Data Analytics course*** <br /> 
***Here I will explain how I came to the solution of given tasks, reference the sources I researched for solving the problems and list the technologies I used for creating and testing the code*** <br />
<br />
<br />

# Table of contents
* [Weekly tasks](#weekly-tasks)
    * [helloworld](#helloworld)
    * [bank](#bank)
    * [Accounts](#accounts)
    * [AccountsExtra](#accountsextra)
    * [Collatz](#collatz)
    * [Weekday](#weekday)
    * [squareroot](#squareroot)
    * [es](#es)
    * [plottask](#plottask)


  


Weekly tasks
======
### ***helloworld***

  
1.The helloworld python program should  display Hello World! when it is run - This is week01 Task <br /> 
<br />
<br />

### ***bank***
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
   Use the floor //100 to get euro value and the modulus % maths function % to return the cents value
   <br />
   <br />
   Concatenate the two variables together to get the monetary amount<br />
   <br />
   Then print the output <br />
   <br />
   print (f' The sum of {amount1} and {amount2} is €{EuroAmount}.{CentAmount}') = €15.89 <br />
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
Print the new variable which is (s)<br /> ![Histogram - Week 08 Task](https://user-images.githubusercontent.com/123590406/226714350-59ec0d1f-826b-4773-86d2-ba9c0ce95bc5.png)

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
There is some error handling in this program and I referenced stackoverflow (https://stackoverflow.com/questions/4097461/printing-out-actual-error-message-for-valueerror) and also W3schools for formatting of the query <br />
<br />
If the user inputs a negative number or a string the program throws a warning message back to the user <br />
<br />
If number is not divisable by 2 then it is odd - Multiply by 3 and add 1 <br />
<br />
If number is divisable by 2 then it is even so then the program will divide by 2<br />
<br />
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

### ***squareroot*** 

6. The squareroot python progam takes the input from the user which is a positive floating-point number as input and outputs an approximation of its square root. <br />The method that is to be used is the newton method. Newton's method works by taking an estimate of the root of the equation and calculating a more accurate estimate, a process that can be repeated to approximate the true value of the root more precisely. <br />
<br />
Main reference for my work for this task was th website www.geeksforgeeks.org and also www.w3schools.com
<br />
<details>
           <summary>Details of Input and Output</summary>
</p> 

There is an inbuilt function in Python which can calculate the square root we were tasked to create our own function using Newtons method<br />
<br />
<br />
#Newton’s Method is described below: <br />
Let N be any number then the square root of N can be given by the formula: <br />
root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1. <br />
<br />
<br />   
The name of the function is sqrt
<br />   
Assuming the sqrt of n as n only <br /> 
Assign X to the N itself.<br /> 
<br /> 
<br /> 
x = n
<br /> 
<br /> 
To count the number of iterations/loops<br /> 
Start a loop and keep calculating the root which will surely move towards the correct square root of N<br /> 
<br /> 
<br /> 
    count = 0<br /> 
 <br /> 
 <br /> 
    while (1) :<br /> 
        count += 1<br /> 
        <br /> 
        <br /> 
 
     Calculate more closed x   <br /> 
        <br /> 
        <br /> 
        root = 0.5 * (x + (n / x))<br /> 
 <br /> 
 <br />         
Check for the difference between the assumed X and calculated root, if not yet inside tolerance then update root and continue <br /> 
If the calculated root comes inside the tolerance allowed then break out of the loop <br /> 
<br /> 
<br />
</details>
<br />

### ***es*** 

7. The es python progam reads in a text file (.txt) and outputs the number of  'e's' that are in the text file.<br />
The filename is taken from an argument on the command line arg = sys.argv[1] - From the first argument so it ignores the name of the 
Python program in the command line <br />
<br />
Main reference for my work for this task was the website www.geeksforgeeks.org and also www.w3schools.com <br /> 
<br /> 
I also looked at a utube video which showed how to pass an argument in from the command line <br /> 
<br /> 
The request was to just pass in one argumnt which was the name of the file but I have also passed in the letter<br /> 
<br /> 
The utube video is located at https://www.youtube.com/watch?v=QJBVjBq4c7E
<br />
<br />
<details>
           <summary>Details of Input and Output</summary>
</p> 
<br />
<br />
Import sys in order to pass an argument from the command line   <br />
I am going to pass in two arguments here<br />
<br />
1. is the name of the file (arg) and
<br />
2. is the letter that will be searched for(letter) <br />
<br />
There is also some error handling done in the script - If the filename does not exist it warns the user to enter another filename <br />
<br />
This is done by importing the os function  <br /> 
<br /> 
<br />
</details>
<br />

### ***plottask***   

8. # plottask.py 
The plottask program creates a histogram with a normal distribution of 1000 values with a mean of 5 and a standard deviation of 2
Plot of the function  h(x)=x3 in the range [0, 10] <br />
<br /> 
Main reference for my work for this task were the below sites<br /> 
https://www.w3schools.com/python/matplotlib_histograms.asp<br /> 
https://www.geeksforgeeks.org/how-to-set-axis-ranges-in-matplotlib/<br /> 
https://stackoverflow.com/questions/30765455/why-is-my-plt-savefig-is-not-working <br /> 
<br /> 
<br /> 
<details>
           <summary>Details of Input and Output</summary>
</p> 
<br />
<br />
***Import Numpy and Matplotlib***
   <br />
Import Numpy to create arrays and mathmatical functions<br />
<br />
Import matplotlib to create visualisations in Python<br />
<br />
1. Create an array using Numpy - Array from 0-11<br />
xpoints = np.array(range(0, 11))<br />
<br />
2.  Y Axis is the Cube of the value on the X Axis<br />
ypoints = xpoints ** 3    <br />
<br />
3.Plot the points add the colour - Also the legend <br />
plt.plot(xpoints, ypoints, color='r', label = "x cubed")
<br />
<br />
4. Set the values - Mean, Std Deviation and Total<br />
<br />
Mean = 5<br />
StdDev = 2<br />
Total = 1000  <br />
 <br />
5. Code is entered below so that the "random" numbers are the same each time<br />
<br />
np.random.seed(1)<br />
<br />
6. Set titles and labels and create histogram through matplotlib<br />
<br />
plt.title("Week 08 Task - Programming and Scripting", color='black')<br />
<br />
plt.xlabel("X = Range 0-10") # Label for X Axis<br />
<br />
plt.ylabel("Y = X Cubed") # Label for Y Axis<br />
<br />
plt.legend() # Show the Legend<br />
<br />
plt.grid() # Show gridlines on Histogram<br />
<br />
plt.hist(x) # Histogram<br />
<br />
plt.savefig('plottask.png') # Save to PNG file<br />
<br />
plt.show() # Show must be after the savfig or it comes out blank<br />

Output as shown below.

![plottask](https://user-images.githubusercontent.com/123590406/226714468-582f2977-1a4d-4b16-a119-9f161105e1ac.png)
