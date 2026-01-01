# u = initial velocity  , v = final velocity , a = acceleration  , d = displacement

u = float(input("Enter initial Velocity : "))
v = float(input("Enter final Velocity : "))
a = float(input("Enter acceleration : "))

d = (v**2 - u**2) / (2*a)
print("displacement is : " , d)
