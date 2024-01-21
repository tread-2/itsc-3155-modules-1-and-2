user_input = input("Enter a string: ")

# Seperate lowercase and uppercase letters
lowercase = ''.join(char for char in user_input if char.islower())
uppercase = ''.join(char for char in user_input if char.isupper())

# Remove spaces
no_spaces = user_input.replace(" ", "")

# Constructing lowercase letters in the front
result = lowercase + uppercase + no_spaces

# Print results
print(result)
