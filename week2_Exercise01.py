# We'll make a fucntion that would find unique intger values within the users list, when the user has entered there integers it will find elements that are not in the list and print them out
def get_unique_elements(input_list):
    # Istantiate an empty list, let users fill in this list
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

user_input = input("Enter some integers sperated by spaces: ")
user_list = [int(x) for x in user_input.split()] # Simply taking inputed integers and converting it into a readable integer strings

# Call the get_unique_elements function with the users inputted list
result = get_unique_elements(user_list)

# Print results
print("User input list:", user_list)
print("List with unique elements:", result)