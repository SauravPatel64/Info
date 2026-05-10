"""
3. Employee Bonus Distribution System
A company provides bonuses based on years of experience.
Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus
"""

yrs = int(input("Enter your Experience = "))

print("30% bonus" if yrs> 10 else "20% bonus" if  yrs>5 else "10% bonus")