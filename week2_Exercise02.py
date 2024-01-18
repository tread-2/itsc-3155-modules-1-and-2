# Function to call an empty dict (hashmap), this will copmbine dicts1 and dicts2 together
def combine_dicts(dicts1, dicts2):
    combined_dicts = {}

# Basic iterations through keys in dicts1
    for key in dicts1:
        if key in dicts2:
            # Adding common keys if there common
            combine_dicts[key] = dicts1[key] + dicts2[key]
    return combined_dicts

# User input for creating the dict1
dicts_input1 = input("Enter values for dicts1 (key pairs seperated by commas): ")
dicts1 = dict(item.split(":") for item in dicts_input1.split(",")) # Formatting the input so that each key-value is speperated by commas

# User input for creating the dict2
dicts_input2 = input("Enter values for dicts2 (key pairs seperated by commas): ")
dicts2 = dict(item.split(":") for item in dicts_input2.split(","))

# Calling the combine_dicts function from dicts1 and dicts2 user entries
combined = combine_dicts(dicts1, dicts2)

# Print results
print("Combined:", combined)