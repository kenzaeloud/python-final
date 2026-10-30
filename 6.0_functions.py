"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of expense amounts (numbers), for example [12.5, 3.0, 8.4].
# 2. Process: it adds all the amounts and divides by how many amounts there are.
# 3. Out: the average amount, as a number. If the list is empty, it returns None.
# 4. My function name, and why return rather than print: average_amount. The name says what it does. I return the result instead of printing it, because then I can use it in other code (to compare it, or to save it). If I only print, the result is lost.


# Your code below
# Computes the average of a list of amounts.
# It returns the result (it does not print it). If the list is empty, it returns None.
def average_amount(amounts):
    if len(amounts) == 0:
        return None
    return sum(amounts) / len(amounts)


# I call the function three times with different lists and show the results.
result_1 = average_amount([12.5, 3.0, 8.4])
result_2 = average_amount([10, 20])
result_3 = average_amount([5])

print("Average 1:", round(result_1, 2))
print("Average 2:", round(result_2, 2))
print("Average 3:", round(result_3, 2))

# Check with an empty list:
print("Average of an empty list:", average_amount([]))

# Check: with an empty list, the function returns None and does not crash.
# I think this is acceptable, because there is no average of nothing,
# and the code that calls the function can test for None.