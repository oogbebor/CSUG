total_rainfall = 0
num_years = int(input("Enter the number of years: "))
for year in range(num_years):
    for month in range(12):
        rainfall = float(input(f"Enter rainfall for month {month + 1} of year {year + 1} in inches/ft: "))
        total_rainfall += rainfall
total_months = num_years * 12
average_rainfall = total_rainfall / total_months

print(f"Total number of months: {total_months}")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")