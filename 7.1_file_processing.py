"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Some names are in capital letters and some in small letters.
# - Some lines have spaces at the beginning.
# - There are empty lines.
# - Guido van rossum has 3 words, so it is not clear which one is the last name.

# 1. In: the file names.txt, with one name per line. The names are messy.
# 2. Process, problem by problem:
#    - capital and small letters: I change each name to the same style (first letter in capital).
#    - spaces at the beginning: I remove them with strip().
#    - empty lines: I skip them.
#    - a name with 3 words: I take the last word as the last name.
# 3. Out: a new file sorted_names.txt with the clean names, sorted by last name. names.txt is not changed.
# 4. How I decide which word is the last name: it is the last word of the line. For Guido van rossum, the last name is rossum.


# Your code below
INPUT_FILE = "names.txt"
OUTPUT_FILE = "sorted_names.txt"


# Reads the file and returns the list of lines. The original file is not changed.
def load_lines(path):
    with open(path, encoding="utf-8") as f:
        return f.readlines()


# Cleans one line: removes the spaces at the beginning and at the end,
# and puts every word in the same style (first letter in capital).
def clean_name(line):
    return line.strip().title()


# Cleans all the lines and skips the empty ones.
def clean_lines(lines):
    names = []
    for line in lines:
        name = clean_name(line)
        if name == "":
            continue
        names.append(name)
    return names


# The last name is the last word of the name.
def last_name(name):
    return name.split()[-1]


# Sorts the names by last name.
def sort_names(names):
    return sorted(names, key=last_name)


# Writes the names in a new file, one name per line.
def save_names(names, path):
    with open(path, "w", encoding="utf-8") as f:
        for name in names:
            f.write(name + "\n")


# Runs the steps in order and shows how many lines went in and out.
def main():
    lines = load_lines(INPUT_FILE)
    names = sort_names(clean_lines(lines))
    save_names(names, OUTPUT_FILE)
    print(len(lines), "lines in", INPUT_FILE, "->", len(names), "names in", OUTPUT_FILE)


if __name__ == "__main__":
    main()

    # Check: names.txt has 10 lines and sorted_names.txt has 8 lines. The difference is the 2 empty lines, which I skip.
# The first name of the sorted list is Margaret Hamilton and the last one is Alan Turing (sorted by last name).