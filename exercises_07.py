# create a list that we can store values in it
stored_numbers = []

# start the loop from here
while True:
    userInput = input("Enter an integer (type 'QUIT) to stop): ")

    # checking to see if the user wants to quit
    if userInput.upper() == 'QUIT':
        break

    try:
        number = int(userInput)
        stored_numbers.append(number)
    except ValueError:
        print("Invalid input!")

# Create a list of even numbers
even_numbers = [num for num in stored_numbers if num % 2 == 0]

# Print both lists
print("All numebers:", stored_numbers)
print("Even numbers:", even_numbers)