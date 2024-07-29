def tax_calculator(income):
    tax = 0

    # Tax bracket limits and rates
    brackets = [
        (50000, 0.51),  # Above 50,000 NIS
        (35000, 0.45),  # 35,000 to 50,000 NIS
        (25000, 0.40),  # 25,000 to 35,000 NIS
        (18000, 0.30),  # 18,000 to 25,000 NIS
        (12000, 0.20),  # 12,000 to 18,000 NIS
        (6000, 0.10)  # 6,000 to 12,000 NIS
    ]

    # Calculate tax based on the brackets
    for limit, rate in brackets:
        if income > limit:
            tax += (income - limit) * rate
            income = limit

    return tax


# Collect salary from the user and calculate tax
try:
    salary = float(input("Enter your salary in NIS: "))
    if salary < 0:
        raise ValueError("Income cannot be negative.")
    tax_due = tax_calculator(salary)
    print(f"Total tax to pay: NIS {tax_due:.2f}")
except ValueError as e:
    print(f"Invalid input: {e}")

