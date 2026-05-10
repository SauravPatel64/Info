"""
7. University Result Classification System

A university assigns final class based on marks, backlog, and project score.

If marks are 75 or above, then check backlog. If backlog is 0, then check project score. If project score is 80 or above, assign First Class with Distinction; otherwise First Class. If backlog is not 0, assign First Class.

If marks are between 60 and 74, then check backlog. If backlog is less than or equal to 2, assign Second Class; otherwise Pass Class.

If marks are between 50 and 59, assign Pass. Otherwise Fail.

Input:
Marks = 78
Backlogs = 0
Project = 85

Output:
Result = First Class with Distinction
"""


marks = int(input("Marks = "))
backlogs = int(input("Backlogs = "))
project_score = int(input("Project = "))


if marks >= 75:
    if backlogs == 0:
        if project_score >= 80:
            result = "First Class with Distinction"
        else:
            result = "First Class"
    else:
        result = "First Class"

elif 60 <= marks <= 74:
    if backlogs <= 2:
        result = "Second Class"
    else:
        result = "Pass Class"

elif 50 <= marks <= 59:
    result = "Pass"

else:
    result = "Fail"


print(f"Result = {result}")