"""
campaign_audit.py - Campaign Audit Quiz

   This program reads the campaigns file, calculates CTR, CPA and ROAS,
   asks 5 questions to the player and gives the score,
   then it saves the result in result.csv.

What is missing: nothing, the program is complete.
"""

import csv
import os
from datetime import date

CSV_FILE = "campaigns_A.csv"
RESULT_FILE = "result.csv"


# ---------------------------------------------------------------------------
# 1. READING THE DATA
# ---------------------------------------------------------------------------
# Changes the text from the CSV into a number (comma becomes a dot).
# If the cell is empty or not a number, it gives None so the program does not crash.
def parse_number(text):
    """Convert a raw cell like '11088,60' into a float.
    Returns None if the cell is empty or not a number (no crash)."""
    if text is None:
        return None
    text = text.strip().replace(" ", "").replace(",", ".")  # European decimal comma
    if text == "":
        return None
    try:
        return float(text)
    except ValueError:
        return None

# Reads the CSV file (separator ;) and returns a list of campaigns.
# Numbers are converted with parse_number.
def read_campaigns(path):
    """Read the raw CSV (separator ';', BOM, an empty column) and return a list
    of dicts with clean numeric values. Raises FileNotFoundError if missing."""
    campaigns = []
    # utf-8-sig removes the invisible BOM at the start of the file
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            # we use the header names, so the empty column between
            # Conversions and Revenue is simply ignored
            name = (row.get("Campaign") or "").strip()
            if name == "":  # completely empty line
                continue
            campaigns.append({
                "name": name,
                "channel": (row.get("Channel") or "").strip(),
                "impressions": parse_number(row.get("Impressions")),
                "clicks": parse_number(row.get("Clicks")),
                "cost": parse_number(row.get("Cost (€)")),
                "conversions": parse_number(row.get("Conversions")),
                "revenue": parse_number(row.get("Revenue (€)")),
            })
    return campaigns


# ---------------------------------------------------------------------------
# 2. COMPUTING THE INDICATORS
# ---------------------------------------------------------------------------
# Computes CTR, CPA and ROAS for each campaign.
# Removes campaigns without impressions. If 0 conversions, CPA stays None.
def compute_metrics(campaigns):
    """Add ctr, cpa, roas to each campaign and return only the valid ones.
    Rule 1: empty impressions -> campaign excluded from everything.
    Rule 2: zero conversions -> cpa = None (excluded from CPA only)."""
    valid = []
    for c in campaigns:
        if c["impressions"] is None or c["impressions"] == 0:
            continue
        c["ctr"] = c["clicks"] / c["impressions"]
        if c["conversions"]:  # None or 0 -> no CPA
            c["cpa"] = c["cost"] / c["conversions"]
        else:
            c["cpa"] = None
        c["roas"] = c["revenue"] / c["cost"] if c["cost"] else None
        valid.append(c)
    return valid


# ---------------------------------------------------------------------------
# 3. COMPUTING THE CORRECT ANSWERS (written nowhere, computed here)
# ---------------------------------------------------------------------------
# Finds the 5 correct answers of the quiz from the campaigns.
def compute_answers(valid):
    """Return the five correct answers computed from the valid campaigns."""
    best_ctr = max(valid, key=lambda c: c["ctr"])["name"]

    with_cpa = [c for c in valid if c["cpa"] is not None]
    worst_cpa = max(with_cpa, key=lambda c: c["cpa"])["name"]

    roas_above_3 = sum(1 for c in valid if c["roas"] is not None and c["roas"] > 3)

    totals = {}
    for c in valid:
        totals[c["channel"]] = totals.get(c["channel"], 0) + (c["conversions"] or 0)
    top_channel = max(totals, key=totals.get)

    avg_ctr = round(sum(c["ctr"] for c in valid) / len(valid), 2)
    # NB: CTR is a ratio (0.0x). See note in main() about the percent version.

    return [best_ctr, worst_cpa, roas_above_3, top_channel, avg_ctr]


# ---------------------------------------------------------------------------
# 4. THE QUIZ
# ---------------------------------------------------------------------------

QUESTIONS = [
    "1. Which campaign has the best CTR?",
    "2. Which campaign has the highest CPA?",
    "3. How many campaigns have a ROAS above 3?",
    "4. Which channel generated the most conversions in total?",
    "5. What is the average CTR across all campaigns (in %, two decimals)?",
]

# Compares the player's answer with the correct one, without crashing.
def check_answer(index, given, correct):
    """Compare the player's answer with the correct one. Never crashes."""
    given = given.strip()
    if index == 2:  # integer answer
        try:
            return int(given) == correct
        except ValueError:
            return False
    if index == 4:  # decimal answer, accept comma or dot, and a trailing %
        number = parse_number(given.replace("%", ""))
        return number is not None and abs(number - correct) < 0.005
    return given.lower() == str(correct).lower()  # text answers

# Asks the 5 questions and returns the score.
def play_quiz(answers):
    """Ask the 5 questions and return the score."""
    score = 0
    for i, question in enumerate(QUESTIONS):
        try:
            given = input(question + " ")
        except EOFError:
            given = ""
        if check_answer(i, given, answers[i]):
            print("  Correct!")
            score += 1
        else:
            print(f"  Wrong. Correct answer: {answers[i]}")
    return score


# ---------------------------------------------------------------------------
# 5. SAVING THE RESULT
# ---------------------------------------------------------------------------
# Writes the name, score and date in result.csv.
def save_result(player, score, path=RESULT_FILE):
    """Write player name, score and date in result.csv (header added once)."""
    is_new = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["player", "score", "date"])
        writer.writerow([player, score, date.today().isoformat()])


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
# Runs all the steps in order and shows which function fails.
def main():
    try:
        campaigns = read_campaigns(CSV_FILE)
    except FileNotFoundError:
        print(f"Error in read_campaigns: file {CSV_FILE} not found.")
        return

    try:
        valid = compute_metrics(campaigns)
        answers = compute_answers(valid)
        # Q5 is asked in percent -> convert the stored ratio
        answers[4] = round(sum(c["ctr"] for c in valid) / len(valid) * 100, 2)
    except Exception as e:
        print(f"Error in compute_metrics / compute_answers: {e}")
        return

    player = input("Player name: ").strip() or "anonymous"
    score = play_quiz(answers)
    print(f"\nFinal score: {score}/5")

    try:
        save_result(player, score)
    except OSError as e:
        print(f"Error in save_result: {e}")


if __name__ == "__main__":
    main()
