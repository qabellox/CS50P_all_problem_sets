# Get filename from user
file = input("File name: ")
# Remove leading/trailing whitespace
file = file.strip()
# Convert to lowercase for case-insensitive checking
file = file.lower()

# Check file extension and print corresponding media type
if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg"):
    print("image/jpeg")
elif file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
# Default for unknown file types
else:
    print("application/octet-stream")
