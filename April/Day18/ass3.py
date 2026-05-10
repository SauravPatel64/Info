"""
3. A smart electricity monitoring system categorizes usage levels for better energy management. 
The system should take the number of units consumed as input. If the units are greater than or equal to 100, then check further.
 If the units are greater than or equal to 300, assign "High Usage". Otherwise, check again. 
If the units are greater than or equal to 200, assign "Moderate Usage"; otherwise, assign "Normal Usage".
 If the units are less than 100, assign "Low Usage". Display the usage category.

Input:
Units = 220

Output:
Usage Category = Moderate Usage
"""


units =  int(input("Units = "))


if units >= 300:  # Highest threshold checked first
    print("High Usage")
elif units >= 200:
    print("Moderate Usage")
else:
    print("Low Usage")
