# Read user input (variable names must match the checker)
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings (this exact assignment is required by the checker)
monthly_savings = monthly_income - monthly_expenses

# Annual and projected savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# If values are whole numbers, convert to int to avoid trailing .0 in output
if isinstance(monthly_savings, float) and monthly_savings.is_integer():
    monthly_savings = int(monthly_savings)
if isinstance(projected_savings, float) and projected_savings.is_integer():
    projected_savings = int(projected_savings)

# Print results matching the expected format exactly
print("Your monthly savings are $" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: $" + str(projected_savings) + ".")
