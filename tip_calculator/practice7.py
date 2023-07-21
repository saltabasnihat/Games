# Create a program using maths and f-Strings that tells us how many days,
#  weeks, months we have left if we live until 90 years old.
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.

age = input("What is your current age? ")

new_age = int(age)

days = (90 - new_age) * 365
weeks = (90 - new_age) * 52
months = (90 - new_age) * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")