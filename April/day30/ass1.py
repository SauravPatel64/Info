"""
1.Leap Year Event Scheduler – Multi-Year Analysis System

A city event management system schedules special festivals only in leap years.

To plan future events, the system analyzes multiple years instead of just one.

Write a program to:

- Read start year and end year from user
- For every year in the range, check whether it is a Leap Year or Not 
- Apply rules:
    - Divisible by 4 → Leap Year candidate  
    - Divisible by 100 → Not Leap Year  
    - Divisible by 400 → Leap Year  

- If leap year → print year with "Event Scheduled"
- Else → print year with "No Event"

- After checking all years:
    - Count total leap years
    - Print total events scheduled

Input:
2000
2005

Output:
2000 → Event Scheduled
2001 → No Event
2002 → No Event
2003 → No Event
2004 → Event Scheduled
2005 → No Event

Total Leap Years = 2
Total Events Scheduled = 2
"""


startYear = int(input("Enter Starting Year = "))
endYear = int(input("Enter Ending Year = "))

i = startYear
loop = 0
event = 0
while i<= endYear:
    if (i%4==0) or (i%400==0) and (i%100==0) :
        print(f"{i} -> Event Scheduled")
        i+=1
        loop += 1
        event += 1
    else:
        print(f"{i} -> No Event")
        i+=1
        
print(f"Total Leap Years = {loop}")
print(f"Total Event Scheduled = {event}")



