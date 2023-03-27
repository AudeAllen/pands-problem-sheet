# Function to return the square root of a number using Newtons method
# Newton’s Method: 
# Let N be any number then the square root of N can be given by the formula: 
# root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1. 
 
#Author: Audrey Allen

# Name of function is sqrt 



def sqrt(n, l) :
 
    # Assuming the sqrt of n as n only
    # Assign X to the N itself.
    x = n
 
    # To count the number of iterations/loops
    # start a loop and keep calculating the root which will surely move towards the correct square root of N

    count = 0
 
    while (1) :
        count += 1
 
        # Calculate more closed x
        root = 0.5 * (x + (n / x))
 
        # Check for the difference between the assumed X and calculated root, if not yet inside tolerance then update root and continue
        # If the calculated root comes inside the tolerance allowed then break out of the loop

        if (abs(root - x) < l) :
            break
 
        # Update root
        x = root
 # Return the root
    return root

    print(sqrt(n, l))
 
# Main piece of code which asks the user to input a float to get the square root

if __name__ == "__main__":
    n = float(input('Enter number please: '))

    l = 0.00001

 # Print the root

    print(sqrt(n, l))

    print("The square root of n using the Newton method is ")
    
    print(sqrt(n, l))


