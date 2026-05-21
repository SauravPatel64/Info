""" 
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won won won the match and india created history
Output:
india
"""

s = input("Enter Sentence : ")

rep = ""
ls = s.split()

high = 0

for ch in ls:
    count = 0
    for w in ls:
        if ch == w:
            count=count+1
    if count>high:
        rep = ch
        high = count
    
print(rep)    