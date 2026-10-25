MIN_DISCOUNT_SEATS = 10
HIGH_DISCOUNT_SEATS = 50
STANDARD_DISCOUNT = 0.07
EDUCATION_DISCOUNT = 0.16
NO_DISCOUNT = 0.0
ONBOARDING_THRESHOLD = 400.0
ONBOARDING_FEE = 60.0
CONTRACT_REVIEW_THRESHOLD = 5000.0
TRAINER_MIN_SEATS = 25
TRAINER_TOTAL_THRESHOLD = 3000.0


def calculate_license_cost(seat_price: float, seats: int) -> float:
    """Return the license coast before any discount."""
    return seat_price * seats


def get_seat_discount(seats: int, education: bool = False) -> float:
    """Return the discount rate based on seats and education status."""
    if seats < MIN_DISCOUNT_SEATS:
        return NO_DISCOUNT
    if seats >= HIGH_DISCOUNT_SEATS and education:
        return EDUCATION_DISCOUNT
    return STANDARD_DISCOUNT


def calculate_license_total(seat_price: float, seats: int, education: bool = False) -> float:
    """Return the discounted license total including any onboarding fee."""
    cost = calculate_license_cost(seat_price, seats)
    discount = get_seat_discount(seats, education)
    discounted_cost = cost * (1 - discount)

    if discounted_cost <= ONBOARDING_THRESHOLD:
        return discounted_cost + ONBOARDING_FEE

    return discounted_cost


def needs_contract_review(total: float) -> bool:
    """Return True when the license total requires a contract review."""
    return total > CONTRACT_REVIEW_THRESHOLD


def gets_trainer(seats: int, total: float) -> bool:
    """Return True when an order qualifies for a dedicated trainer."""
    return seats >= TRAINER_MIN_SEATS or total > TRAINER_TOTAL_THRESHOLD


def total_licensed(orders: list) -> float:
    """Return the total license revenue from all orders."""
    total = 0.0

    for order in orders:
        license_total = calculate_license_total(
            order["seat_price"],
            order["seats"],
            order["education"]
        )
        total += license_total

    return total


def largest_license(orders: list) -> str:
    """Return the company with the largest license total."""
    largest_total = 0.0
    largest_company = ""

    for order in orders:
        total = calculate_license_total(
            order["seat_price"],
            order["seats"],
            order["education"]
        )

        if total > largest_total:
            largest_total = total
            largest_company = order["company"]

    return largest_company


def format_license_line(
    company: str,
    total: float,
    contract_review: bool,
    trainer: bool
) -> str:
    """Format one line of the license report."""
    review_text = "yes" if contract_review else "no"
    trainer_text = "yes" if trainer else "no"

    return (
        f"{company}: ${total:.2f} | "
        f"contract review: {review_text} | "
        f"trainer: {trainer_text}"
    )
