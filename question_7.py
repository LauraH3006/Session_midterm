import random

# Create an empty list to store random numbers
random_numbers = []

# Generate 10 random numbers between 1 and 100
for i in range(10):
    random_numbers.append(random.randint(1, 100))  #append allows to add single elements

# Iterate through the list and modify values based on conditions
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        # Replace numbers greater than 50 with a new random number between 20 and 30
        random_numbers[i] = random.randint(20, 30)
    else:
        # Replace numbers lower than 50 with "XX"
        random_numbers[i] = "XX"

# Print the final list
print(random_numbers)
