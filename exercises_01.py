grade = int(input("Enter a grade: "))

if(grade >= 90):
    print("Your grade is: A")
elif grade >= 80 or  grade <= 90:
    print("Your grade is: B")
elif grade >= 70 or  grade <= 80:
    print("Your grade is: C")
elif grade >= 60 or  grade <= 70:
    print("Your grade is: D")
else:
    print("Your grade is: F")
