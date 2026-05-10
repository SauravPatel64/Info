"""
Assignment 6: Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0

"""

data = int(input("Data = "))

mb = 1024
kb = mb * 1024

data_mb = float(data * mb)
data_kb = float(data * kb)

# Display results
print(f"In MB = {data_mb}")
print(f"In KB = {data_kb}")