
"""
7.
=========================================
MISSING ALPHABET FINDER
=========================================

Enter a sentence and find which
alphabets are missing.

Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit

Requirements:
- Use Set containing a-z

"""
alpha=set("abcdefghijklmnopqrstuvwxyz")
sen=set()
while True:
    print("Menu:")
    print("1. Enter Sentence")
    print("2. Display Missing Alphabets")
    print("3. Count Missing Alphabets")
    print("4. common in both")
    print("exit")
    
    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            s=input("enter your sentence")
            sen=set(s)
        case 2:
            a=alpha-sen
            print("missing alphabet",a)
        case 3:
            print(len(a))
        case 4:
            print("common in both",alpha&sen)
        case 5:
            print(exit)
            break