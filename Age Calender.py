age = int(input("What is your current age ? "))
years_remaining = 90 - age
days_remaining = 365 * years_remaining
weeks_remaining = 52 * years_remaining
months_remaining = years_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left.")