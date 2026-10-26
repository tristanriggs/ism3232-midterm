# ISM3232 Midterm: [Cloudstep Software]

- **Name:** [Tristan Riggs]
- **Version:** [1.0]
- **Date:** [10/25/2026]

## What This Program Does
Calculates software license costs, applies discounts and fees, and determines contract reviews and trainer eligibility.
## Business Rules
The license cost is the price per seat times the number of seats.
The discount depends on the number of seats:
Seats	Discount
Fewer than 10 seats	No discount
10 through 49 seats	7%
50 seats or more	16%
The 16% discount is only for education customers. Any other order of 50 seats or more gets the 7% discount.
A $60 onboarding fee is added when the discounted cost is $400 or less.
A license total of more than $5,000 needs a contract review.
An order gets a dedicated trainer when it has 25 seats or more or its license total is over $3,000.
## How to Run
source .venv/bin/activate
python3 main.py
## How to Test
ruff format .
ruff check .
pytest -v
## Files in This Repository
business_rules.py 
main.py 
commands.md 
README.md
requirements.txt
.gitignore 
tests/__init__.py 
tests/test_business_rules.py 
## AI Use Statement
I did not use AI on this assignment. 