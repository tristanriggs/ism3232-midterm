from business_rules import (
    calculate_license_cost,
    calculate_license_total,
    format_license_line,
    get_seat_discount,
    gets_trainer,
    largest_license,
    needs_contract_review,
    total_licensed,
)


def test_calculate_license_cost():
    assert calculate_license_cost(40.0, 5) == 200.0


def test_get_seat_discount():
    assert get_seat_discount(5) == 0.0
    assert get_seat_discount(20) == 0.07
    assert get_seat_discount(60, True) == 0.16
    assert get_seat_discount(60, False) == 0.07


def test_license_cost_zero_seats():
    assert calculate_license_cost(40.0, 0) == 0.0


def test_license_cost_multiple_seats():
    assert calculate_license_cost(50.0, 10) == 500.0


def test_discount_below_20_seats():
    assert get_seat_discount(9) == 0.0


def test_discount_at_20_seats():
    assert get_seat_discount(10) == 0.07


def test_discount_below_50_seats():
    assert get_seat_discount(49, True) == 0.07


def test_discount_at_50_seats():
    assert get_seat_discount(50, True) == 0.16


def test_license_total_no_discount():
    assert round(calculate_license_total(40.0, 5), 2) == 260.00


def test_license_total_with_discount():
    assert round(calculate_license_total(35.0, 12, True), 2) == 450.60


def test_contract_review_at_limit():
    assert needs_contract_review(5000.0) == False


def test_contract_review_above_limit():
    assert needs_contract_review(5000.01) == True


def test_trainer_below_25_seats():
    assert gets_trainer(24, 1000.0) == False


def test_trainer_at_25_seats():
    assert gets_trainer(25, 1000.0) == True


def test_trainer_at_3000_total():
    assert gets_trainer(10, 3000.0) == False


def test_trainer_above_3000_total():
    assert gets_trainer(10, 3000.01) == True


def test_total_licensed_empty_list():
    assert total_licensed([]) == 0.0


def test_total_licensed_one_order():
    orders = [
        {
            "company": "Pine Books",
            "seat_price": 40.0,
            "seats": 5,
            "education": False,
        }
    ]
    assert round(total_licensed(orders), 2) == 260.00


def test_largest_license_empty_list():
    assert largest_license([]) == ""


def test_largest_license_tie():
    orders = [
        {"company": "Alpha", "seat_price": 40.0, "seats": 5, "education": False},
        {"company": "Beta", "seat_price": 40.0, "seats": 5, "education": False},
    ]
    assert largest_license(orders) == "Alpha"


def test_onboarding_fee_at_400():
    assert round(calculate_license_total(400.0, 1), 2) == 460.00


def test_no_onboarding_fee_above_400():
    assert round(calculate_license_total(400.01, 1), 2) == 400.01


def test_format_license_line():
    result = format_license_line("Alpha", 500.0, True, False)
    assert result == "Alpha: $500.00 | contract review: yes | trainer: no"
