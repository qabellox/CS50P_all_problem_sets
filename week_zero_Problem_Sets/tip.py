# Get meal cost from user and remove dollar sign
cost = int(input("How much was the meal? ").replace("$", ""))

# Get tip percentage from user, remove percent sign, and convert to decimal
percentage = int(input("What percentage would you like to tip? ").replace("%", "")) / 100

# Calculate the tip amount
tip = cost * percentage

# Display the result with 2 decimal places
print(f"Leave ${tip:.2f}")
