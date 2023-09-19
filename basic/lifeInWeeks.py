year = int(input("Enter your age: "))

years_reamin = 90-year
days_remain = years_reamin*365
week_reamin = years_reamin*52
month_remain = years_reamin*12

print(f"You have {days_remain} days, {week_reamin} weeks and {month_remain} months")