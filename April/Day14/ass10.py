"""
Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4
"""

t=int(input("Total seconds ="))

h=((t//60)//60)
m=((t//60)%60)
s=(t%60)
print("Hours =",h)
print("minutes =",m)
print("second =",s)
