#)what is a leap year ? => A year in which feb has 29 days instead of 28 days means 366 days acutal day is 365 .242days
#             366 = 365.242
#             366 = 365 + 0.25
#             366 = 365 + 1/4
#             366 = 365 + 1/ 4 * 4
# that means after every 4 year we add 1 tpo compishiyent that
# every year % 4 is leap year after adding 1 day in itz but only according to juliean Calender


# )Juliean Calender => but julian calender was wrong because we approx take 365 .242 as 365.25 means 0.008 extra .
# after 125 year i.e 125 * 0.008  = 1 day . means after 10 century we are addding 10 days extra . so this method is wrong to calculate the leap year

#) Gregoriean Calender =>
#             365.242 days
#             365.25 = 365 +0.25 - 0.01 + 0.002
#      just to understand better . convert into fraction
#             365.242 = 365 + 1/4 - 1/100 + 1/400

#          this isi actual formula followed to calculate the leap the year
# this formula says that .  year divisible by 4 is leap year => 1/4
# this fromula says that , year divisible by 100 is not  leap year  => -1/100
#also it says that , if year is divisible by 400 then it is leap year = + 1/400



#) Check for Leap Year

year = int (input("Enter the Year to check whether the year is leap Year  or not : "))

if year % 100 == 0:
    if year % 400 == 0:
        print("Leap Year")
    else:
        print("Not Leap Year")
elif year % 4 == 0:
    print(" Leap Year")
else:
    print("Not Leap Year")