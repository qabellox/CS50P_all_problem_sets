# Get time from user
def main():
    time = input("What time is it? ")
    # Convert time to hours as a float
    hours = convert(time)
    # Check if it's breakfast time (7:00 to 8:00)
    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    # Check if it's lunch time (12:00 to 13:00)
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    # Check if it's dinner time (18:00 to 19:00)
    elif 18.0 <= hours <= 19.0:
        print("dinner time")

# Convert time string to hours as a float
def convert(time):
    # Split the time at the colon
    hours, minutes = time.split(":")
    # Convert to floats
    hours = float(hours)
    minutes = float(minutes)
    # Return total hours (hours + minutes/60)
    return hours + (minutes / 60)

# Run main when file is executed directly
if __name__ == "__main__":
    main()
