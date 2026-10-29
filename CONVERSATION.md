# CONVERSATION.md: my exchanges with the AI (Claude)

## Context
Final exam, session 8: Campaign Audit Quiz. Dataset: `campaigns_A.csv`.
I used Claude as an assistant. Claude wrote the first version of `campaign_audit.py`.
Then I read it, tested it, and had each function explained step by step until I understood it.
I wrote the comments above each function myself.

## 1. Ask: what I asked
I gave Claude the exam instructions (PDF) and my file `campaigns_A.csv`, and asked it to write
the program: read the CSV, compute CTR / CPA / ROAS, ask 5 questions, give the score,
write `result.csv`.

## 2. Read: what Claude found in the file (it is not clean)
- The separator is `;` and not `,`.
- An invisible character at the start of the file (BOM) -> the file is read with `utf-8-sig`.
- An empty column between `Conversions` and `Revenue (€)` -> columns are read by their name.
- Decimal comma (`11088,60`) -> replaced by a dot before `float()`.
- One campaign without impressions (Monthly Newsletter) -> excluded from all calculations.
- Two campaigns with 0 conversions (Black Friday, App Install) -> no CPA (None), but kept
  for the other calculations. This avoids the `ZeroDivisionError`.

## 3. Adapt: what had to be adapted to MY file
- The exact column names: `Cost (€)`, `Revenue (€)`, `Conversions`.
- Question 5: the instructions do not say if the average CTR is a ratio or a percentage.
  I chose the percentage (2.60 %). If the teacher expects the ratio, only one line in `main()` changes.

## 4. Check: hand verification
I recomputed the values with a small independent script. The results are the same as the program's:
- Best CTR: Aurora Launch (4.07 %)
- Highest CPA: Blog Traffic (49.36 €)
- Campaigns with ROAS > 3: 7
- Channel with the most conversions: YouTube Ads (4125)
- Average CTR: 2.60 %

## 5. Errors and difficult points
- Main risk: dividing by 0 when a campaign has 0 conversions. Fixed with
  `if c["conversions"]:` before the division.
- Second risk: an empty cell or unreadable text in the CSV. Fixed with `parse_number`, which returns `None`
  instead of crashing.
- A first test with wrong answers gave a score of 0/5 without crashing and wrote `result.csv`.
- A mistake I made while editing: I pasted my comments at the end of the `def` line instead of above it.
  The program still ran, but I moved them above each function to keep the code clean.
- In the terminal I once typed `copilot` before my command by mistake. It gave an error, and I fixed it
  by typing only `python campaign_audit.py`.

## 6. What I understood
At the beginning I did not understand the code. Claude explained each function and asked me small questions to check.
The hardest part was the empty cell and the zero conversions, because the program must not crash and i was affraid to click or delete something that will crash the program.
Now I understand for example that parse_number changes the text into a number and gives None when the cell is empty and also that compute_metrics calculates CTR, CPA and ROAS. It skips the campaigns with no impressions, and when conversions is 0 it does not calculate the CPA.
I changed the comments in the code with my own words.