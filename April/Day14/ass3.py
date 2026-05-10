"""
Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2
"""

marks_input = input("Enter marks for 5 subjects separated by space: ")

marks = map(int, marks_input.split())

total = sum(marks)

num_subjects = 5
average = total / num_subjects
percentage = (total / (num_subjects * 100)) * 100

print(f"Total = {total}")
print(f"Average = {average}")
print(f"Percentage = {percentage}")
