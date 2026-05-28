""" 
# 3. Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.
The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.
If no unique digit exists, print:

```text
No unique digit found
```
### Input:
```text
A122334455667789
```

### Output:

```text
8
```

"""

str = input("Enter String : ")
count = 0

for  i in range(len(str)):
    count = 0
    if str[i]>='0' and str[i]<="9":
        j = i+1
        for j in range(len(str)):
            if str[i]==str[j]:
                count += 1
                break
 
        
    if ((str[i]>='0' and str[i]<="9")) and count==0:
        print(str[i])
        break

else:
    print("No unique digit found")
            


























