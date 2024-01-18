# This function will take in the user input and  return a dict that keeps count of each letter (in lower case) excluding spaces
def turn_string_into_dict(dict1):
    string_count = {}
    # Formats the string so no spaces appear
    no_spaced_strings = ''.join(char.lower() for char in dict1 if char.isalpha())
    # Counting each occurenece within the string
    for char in no_spaced_strings:
        string_count[char] = string_count.get(char, 0) + 1
    return string_count

# Taking in user input
user_input = input("Enter a string: ")

# Printing the results
results = turn_string_into_dict(user_input)
print(results)