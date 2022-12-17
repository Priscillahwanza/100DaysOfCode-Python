
age = input("What is your current age? ")

x = input("What is your expected age? ")


x_int = int(x)
age_int = int(age)

days = (x_int*365) - (age_int * 365)
weeks = (x_int*52) - (age_int*52)
months = (x_int*12) - (age_int*12)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
