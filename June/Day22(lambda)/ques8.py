""" 

Assignment 4:
 Lottery Ticket Verification (Count Occurrences Using Recursion)

A lottery company assigns a unique ticket number to every participant. Before announcing the results, the company wants to determine how many times a lucky digit appears in a ticket number. This helps identify tickets eligible for special bonus rewards.

As a software developer, your task is to write a recursive Python program that counts the number of times a given digit appears in the ticket number.

Task

Write a recursive function to count the occurrences of a given digit in a ticket number.

Input Format
The first line contains an integer representing the Ticket Number.
The second line contains an integer representing the Lucky Digit.
Output Format

Display the number of times the lucky digit appears in the ticket number using the format:

Digit <Lucky Digit> appears <Count> times.
Sample Input
Enter Ticket Number:
1122334412

Enter Lucky Digit:
2
Sample Output
Digit 2 appears 3 times.
Sample Input 2
Enter Ticket Number:
987654321

Enter Lucky Digit:
5
Sample Output 2
Digit 5 appears 1 time.
Sample Input 3
Enter Ticket Number:
11111111

Enter Lucky Digit: 
2
Sample Output 3
Digit 2 appears 0 times.
"""



def count_digit_occurrences(ticket, digit):
    """Recursively counts the occurrences of a digit in a ticket number."""
    # Base case: if ticket number becomes 0, stop recursion
    if ticket == 0:
        return 0

    # Check if the last digit matches the lucky digit
    match_found = 1 if (ticket % 10 == digit) else 0

    # Recursive step: strip the last digit and add the match result
    return match_found + count_digit_occurrences(ticket // 10, digit)


# --- Main Program Execution ---
# Handling special edge case where ticket number itself is exactly 0
ticket_num = int(input("Enter Ticket Number:\n"))
lucky_digit = int(input("Enter Lucky Digit:\n"))

# If the ticket number is exactly 0 and lucky digit is 0, count is 1
if ticket_num == 0 and lucky_digit == 0:
    count = 1
else:
    count = count_digit_occurrences(ticket_num, lucky_digit)

# Format the word 'time' vs 'times' dynamically based on standard singular/plural rules
word_times = "time" if count == 1 else "times"

print("Output")
print(f"Digit {lucky_digit} appears {count} {word_times}.")
