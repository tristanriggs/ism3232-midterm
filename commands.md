# Terminal Record: [Cloudtsep Spftware]


## 1. Building the project
## 2. The virtual environment
```type
which python3
```

```text
/home/tristan_riggs/ism3232-midterm/.venv/bin/python3
```

The output shows that Python is running from the project's `.venv` folder, which confirms the virtual environment is active.
## 3. The project structure
 README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py
## 4. Every function and test
'''type
rg 'def'
'''
'''text
'''4:def test_calculate_license_cost():
7:def test_get_seat_discount():
13:def test_license_cost_zero_seats():
16:def test_license_cost_multiple_seats():
19:def test_discount_below_20_seats():
23:def test_discount_at_20_seats():
26:def test_discount_below_50_seats():
30:def test_discount_at_50_seats():
33:def test_license_total_no_discount():
37:def test_license_total_with_discount():
41:def test_contract_review_at_limit():
44:def test_contract_review_above_limit():
47:def test_trainer_below_25_seats():
51:def test_trainer_at_25_seats():
54:def test_trainer_at_3000_total():
58:def test_trainer_above_3000_total():
61:def test_total_licensed_empty_list():
65:def test_total_licensed_one_order():
76:def test_largest_license_empty_list():
80:def test_largest_license_tie():
87:def test_onboarding_fee_at_400():
91:def test_no_onboarding_fee_above_400():
94:def test_format_license_line():
13:def calculate_license_cost(seat_price: float, seats: int) -> float:
18:def get_seat_discount(seats: int, education: bool = False) -> float:
27:def calculate_license_total(seat_price: float, seats: int, education: bool = False) -> float:
39:def needs_contract_review(total: float) -> bool:
44:def gets_trainer(seats: int, total: float) -> bool:
49:def total_licensed(orders: list) -> float:
64:def largest_license(orders: list) -> str:
83:def format_license_line
'''
The business_rules.py file defines 8functions and test_business_rules.py definesnthe 23 tests 
## 5. Which files print
```type
rg -l 'print'
```

```text
main.py
commands.md
```
## 6. The commit history
'''type
git log --oneline
4ffe0c5 (HEAD -> master) Complete Part 4 tests
37452af Complete Part 3 order report
a2c6f61 Complete Part 2 business rules
f9f2a25 set up midterm project structure
'''