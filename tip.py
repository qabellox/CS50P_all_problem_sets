cost = int(input("How much was the meal? ").replace("$", ""))
percentage = int(input("What percentage would you like to tip? ").replace("%", "")) / 100
tip = cost * percentage
print(f"Leave ${tip:.2f}")