# check whether gender is male or female . it can be small or lcapital like M or m and F or f

gender  = input("Enter the gender :")

if (gender == "M" or gender == "m"):
    print("Gender :  Male")
elif (gender == "F" or gender == "f"):
    print("Gender :  Female")
else:
    print("invalid input ")