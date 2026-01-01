#a student can't get negative marks , the marks range is only under 0 to 100

marks = int(input("Enter your marks : "))

if marks >= 0 and marks <= 100:
    print("Valid marks ")
else:
    print("Invalid marks")