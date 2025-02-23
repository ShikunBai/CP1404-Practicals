"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_amount = int(input("How many months? "))

    for month in range(1, month_amount + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes, month_amount)


def calculate_total(incomes):
    """Calculate the cumulative total for each month's income."""
    totals = []
    total = 0
    for income in incomes:
        total += income
        totals.append(total)
    return totals


def print_income_report(incomes, month_amount):
    """Print income report for incomes over a given number of months."""
    print("\nIncome Report\n-------------")
    totals = calculate_total(incomes)
    for month in range(1, month_amount + 1):
        income = incomes[month - 1]
        total = totals[month - 1]
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
