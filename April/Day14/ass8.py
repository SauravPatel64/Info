"""
Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0

"""

p = int(input("Principal = "))
r = int(input("Rate  = "))
t = int(input("Time = "))

ci = p*((1+(r/100))**t)
print(ci)