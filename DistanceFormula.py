#distance formula between two coordinate points
#from java program found at: 

import math

#variables
x1 = 0
x2 = 0
y1 = 0
y2 = 0
d = 0.0

#user input
x1 = int(input("Enter the value for x1: "))
y1 = int(input("Enter the value for y1: "))
x2 = int(input("Enter the value for x2: "))
y2 = int(input("Enter the value for y2: "))

#do the math
d = math.sqrt((x1-x2)**2 + (y1-y2)**2)

#print the result
print("The distance between point (",x1,",",y1,") and (",x2,",",y2,") is ",format(d,".2f"))


#java version of this application available at: 