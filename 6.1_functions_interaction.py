"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the file expenses.csv (from exercise 7.0), with the amount of each expense.
# 2. Process, function by function: read_amounts reads the file and gives the list of amounts. average_amount gives the average of the list. count_above counts how many amounts are above a limit. The fourth function uses these three in this order.
# 3. Out: a number, how many of my expenses are above my average expense.
# 4. The question my fourth function answers: how many of my expenses are above my average? Splitting it in three small functions makes it easier to check, because I can test each one alone.

# Your code below

import csv


# Reads expenses.csv and returns the list of the amounts, as numbers.
def read_amounts(path):
    amounts = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            amounts.append(float(row["amount"]))
    return amounts


# Returns the average of a list of amounts, or None if the list is empty.
def average_amount(amounts):
    if len(amounts) == 0:
        return None
    return sum(amounts) / len(amounts)


# Returns how many amounts in the list are above a limit.
def count_above(amounts, limit):
    count = 0
    for amount in amounts:
        if amount > limit:
            count += 1
    return count


# Answers my question: how many of my expenses are above my average expense?
# It uses the three functions above, one after the other.
def expenses_above_average(path):
    amounts = read_amounts(path)
    average = average_amount(amounts)
    if average is None:
        return 0
    return count_above(amounts, average)


# Test of each small function alone:
print(read_amounts("expenses.csv"))
print(average_amount([12.5, 3.0, 8.4]))
print(count_above([12.5, 3.0, 8.4], 7.97))
print(average_amount([]))
# Test of the fourth function:
print("Expenses above my average:", expenses_above_average("expenses.csv"))

# Tests I used (input -> expected output):
# 1. read_amounts("expenses.csv") -> [12.5, 3.0, 8.4]
# 2. average_amount([12.5, 3.0, 8.4]) -> 7.97 (and average_amount([]) -> None)
# 3. count_above([12.5, 3.0, 8.4], 7.97) -> 2
# The fourth function on my file gives 2.