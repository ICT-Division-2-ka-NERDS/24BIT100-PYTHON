def is_leap_year(year):
    # Leap year logic: divisible by 4 but not by 100, unless divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    # Days in each month for regular and leap years
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_months[1] = 29  # February has 29 days in a leap year
    return days_in_months[month - 1]

def total_days(d, m, y):
    # Calculate total number of days from 01/01/0001 to given date (d, m, y)
    days = 0
    
    # Add days for full years before the current year
    for year in range(1, y):
        days += 366 if is_leap_year(year) else 365
    
    # Add days for months in the current year before the current month
    for month in range(1, m):
        days += days_in_month(month, y)
    
    # Add days for the current month
    days += d
    
    return days

def days_between_dates(date1, date2):
    # Convert the tuple dates into total number of days from base date
    total_days1 = total_days(date1[0], date1[1], date1[2])
    total_days2 = total_days(date2[0], date2[1], date2[2])
    
    # Return the absolute difference
    return abs(total_days2 - total_days1)

# Example usage:
date1 = (1, 1, 2020)  # 1st January 2020
date2 = (1, 1, 2025)  # 1st January 2025

print("Number of days between the two dates:", days_between_dates(date1, date2))
