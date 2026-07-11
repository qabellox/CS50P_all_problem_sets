# Get greeting from user
greeting = input("Greeting: ")
# Convert to lowercase for case-insensitive checking
greeting = greeting.lower()
# Remove leading/trailing whitespace
greeting = greeting.strip()

# Check greeting and output corresponding amount
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
