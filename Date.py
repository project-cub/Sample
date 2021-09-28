# Input date
a = input("Enter the Date in DD MM YYYY format: " ).split(" ")
dd = int(a[0])
mm = int(a[1])
yy = int(a[2])

# Function for Leap year
def leap(y):
    if y%4 == 0 and y%100 != 0:
        leap_year = True
    elif (y%400 == 0):
        leap_year = True
    else:
        leap_year = False
    return leap_year

# Sudeep 
leap_count = 0
previous_year = int(yy-1)
while previous_year > 0 :
    if leap(previous_year) == True:
         leap_count = leap_count + 1
    previous_year = previous_year - 1   

# Calculation for number of days uptill previous month of that year
non_leap = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
yes_leap = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

if leap(yy) == False:
    days = int(non_leap[mm-1])
else:
    days = int(yes_leap[mm-1]) 

# Total number of days from 1 January 1 to entered date
n = (365*(yy-1)) + leap_count + days + dd

# Conditions for Day
if n%7 == 1:
    print("Monday")
elif n%7 == 2:
    print("Tuesday") 
elif n%7 == 3:
    print("Wednesday")      
elif n%7 == 4:
    print("Thrusday")     
elif n%7 == 5:
    print("Friday")     
elif n%7 == 6:
    print("Saturday")  
else:
    print("Sunday")       
