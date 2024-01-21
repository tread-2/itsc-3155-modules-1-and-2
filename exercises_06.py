row = int(input("Enter row number from 1 to 5: "))
column = int(input("Enter column number from 1 to 5: "))

# Prints grid
for i in range (1, 6):
    for j in range (1, 6):
        if i == row and j == column:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print(end="\n")
