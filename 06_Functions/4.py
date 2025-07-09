
def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return f'The year {year} is a leap year'
    else:
        return f'The year {year} is not a leap year'

count = is_leap_year(2020)
print(count)