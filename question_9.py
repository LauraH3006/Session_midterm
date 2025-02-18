def days_since_birth(birthday):
    # Extract the year from the birthday string
    birth_year = int(birthday[-4:])  # Get the last 4 characters and convert to integer

    # Assume current year is 2025
    current_year = 2025

    # Calculate the number of whole years passed
    years_passed = current_year - birth_year - 1  # We exclude the birth year and current year

    # Convert years to days
    days_passed = years_passed * 365  # Assuming no leap years

    return days_passed

# Example usage with your birthday
print(days_since_birth("30-06-2003"))
