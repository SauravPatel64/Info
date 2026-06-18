
"""
7.

A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
 361

 Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
 (103, 'Gill', 120)
 (105, 'SKY', 76)
 """


n=int(input("enter no of player : "))
pla=[]
for i in range(n):
    id=int(input("enter id"))
    name=input("enter player name: ")
    runs=int(input("enter runs: "))
    pla.append((id,name,runs))
    print()
print("all player")
for i in pla:
    print(i)
print()
print("highest score")
max=pla[0][2]
h=0
for i in range(len(pla)):
    a=pla[i][2]
    if max<a:
        max=a
        h=i
print(pla[h])

print("lower score")
min=pla[0][2]
h=0
for i in range(len(pla)):
    a=pla[i][2]
    if min>a:
        min=a
        h=i
print(pla[h])

print()
print("avarage")
sum=0
for i in range(len(pla)):
    a=pla[i][2]
    sum=sum+a
print(sum//len(pla))

print("Players Scoring More Than 50 Runs:")
for i in range(len(pla)):
    a=pla[i][2]
    if a>50:
        print(pla[i])
        