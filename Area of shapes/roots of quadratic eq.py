# quadratic eq : ax^2 + bx + c=0      then what value of x = ?

# eg : 1x^2 - 5x + 6 = 0
# let subsittute x = 2  and x = 3  as x^2 is there we will get 2 roots
# formula for x is :
#                 /-----------
# x1 =      -b + V  b^2 - 4ac
#          -------------------
#                   2a
#                                                    b^2 - 4ac > = 0   but in python for squareroot import the math.sqrt function


#                 /-----------
# x2 =      -b - V  b^2 - 4ac
#          -------------------
#                   2a

import math
a = 1
b = -5
c = 6

print(a,"x^2 +", b ,"x +" ,c , "= 0")

r1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
r2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
print("Roots are : " , r1 , "And " , r2 )

