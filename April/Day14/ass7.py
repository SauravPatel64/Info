"""
Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67

"""
import math
run = int(input("Total runs = "))
overs = float(input("Overs = "))
over = int(overs)
ball = over*6

c = int((overs*10)%10)
totalRuns = c + ball
print(f"Total Balls = {totalRuns}\nRun Rate = {round(run/overs,2)}")