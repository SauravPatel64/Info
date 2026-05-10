"""
6.
Data Validation System – Character Identifier
A system needs to validate user input characters.
If the input is:
Alphabet → display "Alphabet"
Digit → display "Digit"
Otherwise → display "Special Character"
Write a program using inline if to classify the character.
"""

num = input("Input = ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
digit = "0123456789"

print("Alphabet" if num in alphabet else "Digit" if num in digit else "Special Character")

