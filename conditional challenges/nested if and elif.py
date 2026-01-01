# when condition is applied in If block or else block is known as nested loop

temp = float(input("Enter the Temperature : "))

if temp == 25 :
    print("Normal Temperature")
else:
    if temp < 25:
        print("Cold Temperature")
    else:
        print("Hot Temperature")




# if elif ladder

tempp = float(input("Enter the temperature : "))
if tempp==25:
    print("Normal Temperature")
elif tempp < 25:
    print("Cold Temperature")
else:
    print("Hot Temperature")