"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: the date, the category and the amount of one expense, typed by the user.
# 2. Process: the program checks that the amount is a number. If not, it asks again. Then it adds the line at the end of the file.
# 3. Out, file name and columns: expenses.csv with the columns date, category, amount.
# 4. Why these columns, and what this file is for: to follow my expenses. With 200 rows I could see what I spend the most on.


# Your code below

import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"
COLUMNS = ["date", "category", "amount"]


# Asks for the amount until the user types a valid number above 0.
def ask_amount():
    while True:
        text = input("Amount (for example 12.50): ").strip().replace(",", ".")
        try:
            amount = float(text)
        except ValueError:
            print("This is not a number. Try again.")
            continue
        if amount <= 0:
            print("The amount must be more than 0. Try again.")
            continue
        return amount


# Asks for the date (Enter = today), the category and the amount.
def ask_entry():
    today = date.today().isoformat()
    day = input(f"Date (press Enter for today, {today}): ").strip() or today
    category = input("Category (food, transport, ...): ").strip()
    while category == "":
        category = input("Category cannot be empty. Category: ").strip()
    amount = ask_amount()
    return [day, category, amount]


# Adds one line at the end of the file. If the file does not exist yet,
# it writes the header line first (only once).
def save_entry(entry):
    is_new = not os.path.exists(FILE_NAME)
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(COLUMNS)
        writer.writerow(entry)


# Runs the steps in order: ask, then save.
def main():
    entry = ask_entry()
    save_entry(entry)
    print("Saved in", FILE_NAME)


if __name__ == "__main__":
    main()

# Check: I ran the program 3 times. expenses.csv has 1 header line and 3 entries. A wrong amount like abc is refused.