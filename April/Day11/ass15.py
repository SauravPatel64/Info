"""
Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h
"""



distance1 = int(input("Enter Distance 1: "))
time1 = int(input("Enter Time 1: "))

distance2 = int(input("Enter Distance 2: "))
time2 = int(input("Enter Time 2: "))

total_distance = distance1 + distance2
total_time = time1 + time2

average_speed = int(total_distance / total_time)

print("Average Speed =", average_speed, "km/h")