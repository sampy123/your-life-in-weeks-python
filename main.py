age = input("What is your current age ?")
D_age = input("How many years you think you can live ?")

if any(c.isalpha() for c in age) or any(c.isalpha() for c in D_age):
    print("something is wrong.")
else:
    age_as_int = int(age)
    D_age_as_int = int(D_age)

    years_remaining = D_age_as_int - age_as_int
    days_remaining = years_remaining * 365
    weeks_remaining = years_remaining * 52
    months_remaining = years_remaining * 12

    print(f"you have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
