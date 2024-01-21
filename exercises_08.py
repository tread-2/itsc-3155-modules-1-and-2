# Create an empty list
storedNumbers = []

# Take input for 10 integers
for _ in range(10):
    while True:
        userInput = input("Enter an integer: ")

        try:
            numbers = int(userInput)
            storedNumbers.append(numbers)
            break
        except ValueError:
            print("invalid input")

# Creating a list with elements that appear once
numbersAppearedOnce = [num for num in storedNumbers if storedNumbers.count(num) == 1]

print("All numbers:", storedNumbers)
print("Only one appearance:", numbersAppearedOnce)
