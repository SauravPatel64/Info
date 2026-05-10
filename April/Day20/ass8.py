"""


8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot
"""
temp = int(input("Enter temperature: "))

if temp < 0:
    print(f"Weather Condition: Freezing")
elif temp >=0 and temp <= 20:
    print(f"Weather Condition: Cold")
elif temp >= 21 and temp <= 35:
    print(f"Weather Condition: Warm")
else:
    print(f"Weather Condition: Hot")


   

