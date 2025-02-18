# Lists are mutable
my_list = [1, 2, 3]
my_list[0] = 100  # Changing the first element
print(my_list)  # Output: [100, 2, 3]

# Strings are immutable
my_string = "hello"
# my_string[0] = "H"  # This will cause an error
new_string = "H" + my_string[1:]  # Creating a new string instead
print(new_string)  # Output: "Hello"
