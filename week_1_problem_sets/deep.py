# Get answer from user
question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
# Convert to lowercase for case-insensitive checking
question = question.lower()
# Remove leading/trailing whitespace
question = question.strip()

# Check if answer matches any valid format
match question:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

"""
# Alternative version using if/elif/else
question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
question = question.lower()
question = question.strip()

if question == "42" or question == "forty-two" or question == "forty two":
    print("Yes")
else:
    print("No")
"""
