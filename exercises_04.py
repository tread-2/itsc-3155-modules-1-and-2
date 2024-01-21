def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

inputNumber = int(input("Enter a number: "))
floatList = []
for i in range(inputNumber):
    num = float(input(f"Enter float {i + 1}: "))
    floatList.append(num)
print("List: ", floatList)

mean_value = calculate_mean(floatList)
print("Average: ", mean_value)

