"""
5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website

"""

url = input("Enter website: ")
length  = len(url)
print(url[0:3])
print(url[len(url)-4:len(url)])

if url[0:3]=="www" and url[length-4:length]==".com":
    print("Valid Website")
else:
    print("Invalid Website")