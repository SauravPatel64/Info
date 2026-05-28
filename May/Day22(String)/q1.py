""" 

1. Smart Log File Error Pattern Detector

A cybersecurity company stores server logs containing repeated system activity characters.

To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

If multiple substrings have the same length, print the first one found.

 Input:

```text
abcabcbb
```

Output:

```text
abc
```

---
"""

s = input("Enter String : ")
currStr = ""
longStr = ""

for ch in s:
    
    if ch in currStr:
        pos = 0
        for i in range(len(currStr)):
            pos = i
            break
        currStr = currStr[pos+1:]
    
    else:
        currStr = currStr + ch
    
    if len(currStr)>len(longStr):
        longStr = currStr

print(longStr)