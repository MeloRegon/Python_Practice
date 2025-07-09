# Age Verification Script
# Asks the user for their age and validates if they are allowed access (18+).
# Handles invalid inputs and negative values.


try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        print("Access denied. You must be at least 18.")
    else:
        print("Access granted.")

except ValueError as e:
    print(f"Invalid input: {e}")
