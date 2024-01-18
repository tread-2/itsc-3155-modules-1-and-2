# Function that checks for valid inputs, edge case being that if user enters invalid input, it will ask them to enter an valid integer until it is surficed
def valid_input():
    while True:
        user_input = input("Enter an integer: ")
        try:
            return int(user_input)
        except ValueError:
            print("Invalid integer, please enter a valid integer")

# Get 5 valid integers from user input
results = 0
for i in range(5):
    get_valid_input = valid_input()
    results += get_valid_input

# Print out the sum
print(results)