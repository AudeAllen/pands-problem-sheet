# plottask.py 
# This program creates a histogram with a normal distribution of 1000 values with a mean of 5 and a standard deviation of 2
# Plot of the function  h(x)=x3 in the range [0, 10]
# Author: Audrey Allen
 
# Import numpy - To create arrays and mathmatical functions
import numpy as np

#Import matplotlib - Creating visualisations in Python
import matplotlib.pyplot as plt


#Create the array - X- Axis from 0-11
xpoints = np.array(range(0, 11))

# Y Axis is the Cube of the value on the X Axis 
ypoints = xpoints ** 3    # cube each entry

#Plot the points add the colour - Also the legend
plt.plot(xpoints, ypoints, color='r', label = "x cubed")

#Set the values - Mean, Std Deviation and Total

Mean = 5
StdDev = 2
Total = 1000

# this is so that the "random" numbers are the same each time
np.random.seed(1)

x = np.random.normal(Mean, StdDev, Total)

# Set titles and labels 
plt.title("Week 08 Task - Programming and Scripting", color='black')
plt.xlabel("X = Range 0-10") # Label for X Axis
plt.ylabel("Y = X Cubed") # Label for Y Axis
plt.legend() # Show the Legend
plt.grid() # Show gridlines on Histogram
plt.hist(x) # Histogram

plt.savefig('plottask.png') # Save to PNG file

plt.show() # Show must be after the savfig or it comes out blank