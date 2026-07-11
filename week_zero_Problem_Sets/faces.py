# Get user input
text = input()

# Replace :) with 🙂 and :( with 🙁
text = text.replace(":)", "🙂").replace(":(", "🙁")

# Display the result
print(text)
