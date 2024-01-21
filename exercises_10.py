input_string = input("Enter a string: ")

# Converts string into seperate characters 
character_list = list(input_string)

spliced_list = [character_list[i:i+3] for i in range(0, len(character_list), 3)]

print("Original String:", input_string)
print("List of Characters: ", character_list)
print("Result: ", spliced_list)