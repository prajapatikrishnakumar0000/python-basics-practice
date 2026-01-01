 # take day no as input , and print day according to it  like 0 = monday  , 1 = tuesday   , 2 = wednesday , 3 = thursday .....


day_number = int (input("Enter the day number "))

if day_number == 0 :
     print("Monday")
elif day_number == 1 :
     print("Tuesday")
elif day_number == 2 :
     print("Wednesday")
elif day_number == 3 :
     print("Thursday")
elif day_number == 4 :
     print("Friday")
elif day_number == 5 :
     print("Saturday")
else:
     print("Invalid Number")