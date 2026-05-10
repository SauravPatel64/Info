"""
9. Multi-Level Employee Promotion System

A company promotes employees based on experience, rating, projects completed, and salary.

If experience is at least 5 years, then check rating. If rating is at least 4, then check projects. If projects are at least 3, then check salary. If salary is up to 50000, promote with 30 percent hike; otherwise 20 percent hike. If projects are less than 3, promote with 10 percent hike. If rating is below 4, no promotion. If experience is less than 5, then check if rating is 5. If yes, fast track promotion; otherwise no promotion.

Input:
Experience = 6
Rating = 4
Projects = 2

Output:
Promotion Status = Promoted with 10% hike

"""

e=int(input("Experience ="))
r=int(input("Rating ="))
p=int(input("Projecting ="))

if e>=5:
    if r>=4:
        if p>=3:
            if salary==50000:
                print("Promotion Status = 30 percent hike")
            else:
                print("Promotion Status = 20 percent hike")
        else:
            print("Promotion Status =  10 percent hike")
    else:
        print("Promotion Status = no promotion")
else:
    if r==5:
        print("Promotion Status = fast track promotion")
    else:
        print("Promotion Status = no promtion")
