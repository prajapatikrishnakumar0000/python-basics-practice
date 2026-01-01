# in shop discount is given , if amount is less than 1000 then 10% discount is given , if more than 1000 and less than 5000 then 15% discount is applied , if more than 5000 and less than 10000 20% discount is applied , if greater than 10000 than 25% is applied

amount = float(input("Enter the amount "))

if amount < 1000:

    if amount < 0:
        print("Amount cannot be negative")
    else:
        print("You got 10% of dicount :", amount * 0.1)
        amount = amount - amount * 0.1
        print("Total Amount to pay : ", amount)

elif amount >= 1000 and amount < 5000 :
    print("You got 15% of dicount :" ,amount * 0.15 )
    amount = amount - amount * 0.15
    print("Total Amount to pay : ", amount)
elif amount >=5000 and amount < 10000 :
    print("You got 20% of dicount :" ,amount * 0.20 )
    amount = amount - amount * 0.20
    print("Total Amount to pay : ", amount)
else:
    print("You got 25% of dicount :" ,amount * 0.25 )
    amount = amount - amount * 0.25
    print("Total Amount to pay : ", amount)