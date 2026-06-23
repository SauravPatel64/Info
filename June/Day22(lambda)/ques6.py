""" 
Assignment 2: Binary Converter for Embedded System

An embedded systems company develops microcontrollers that understand only binary values. Engineers enter decimal numbers, and the software must convert them into binary before sending them to the device.

As a software developer, write a recursive program to perform this conversion.

Task

Write a recursive function to convert a decimal number into its binary representation.

Input
Enter a decimal number:
25
Output
Binary Number = 11001

Note: Do not use Python's built-in bin() function.
"""
def binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    
    return binary(n // 2) + str(n % 2)

num = int(input("Enter a decimal number:\n"))

if num == 0:
    binary_output = "0"
else:
    binary_output = binary(num)

print("Output")
print(f"Binary Number = {binary_output}")

    