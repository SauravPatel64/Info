"""
6. Weather Monitoring System
   A system checks weather conditions:

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert

Input:
Enter temperature: 32
Enter humidity: 75

Output:
Hot day
High humidity alert

===
"""

t=int(input("Enter temprature:"))
h=int(input("Enter humidity:"))

if t>=30:
    print("Hot day")

if h>=70:
    print("High humadity alert")
