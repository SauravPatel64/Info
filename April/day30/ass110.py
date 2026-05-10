"""
10.
Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit  
        Next 100 units      → ₹7 per unit  
        Above 200 units     → ₹10 per unit  

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge  
        - If units < 50 → give ₹100 subsidy  

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill

---

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700
"""

house = int(input("Enter no. of house = "))
coll = 0
high = 0
h = list(map(int, input("Enter units: ").split()))

for i in range(0,len(h)):
    
    if h[i]<100:
        bill = h*5
        if h[i] < 50:
            sum = 0
            sum = sum + (h[i]*5 - 100)
            print(f"House {i} Bill = {sum}")
            coll += sum
            if high < sum:
                high = sum
        else:
            sum = 0
            sum = sum + (h[i]*5)
            print(f"House {i} Bill = {sum}")
            if high < sum:
                high = sum


    elif h[i]>100 and h[i]<=200:
        sum = 0
        first = 100*5
        second = (h[i]-100)*7
        sum = first + second
        print(f"House {i} Bill = {sum}")
        coll += sum
        if high < sum:
            high = sum

    else:
        sum = 0
        first = 100*5
        second = 100*7
        third = (h[i]-200)*10
        
        sum = first + second + third
   
        if sum > 2000:
            sum = (sum*110/100)
        print(f"House {i} Bill = {sum}")
        coll += sum
        if high < sum:
            high = sum


print(f"Total Collection = {coll}")
print(f"Highest Bill = {high}")

        
























    
