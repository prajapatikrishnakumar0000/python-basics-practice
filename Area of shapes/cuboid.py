#it is 3D object who has l , b and h . to calculate the total surface area of cuboid
# 2* (length * height ) + 2* (lenght * bredath) + 2* (bredath * height)
# therefore taking 2 common :  2 (l*h + l*b + b*h)

length = float(input("Enter length : "))
breadth = float(input("Enter breadth : "))
height = float(input("Enter height : "))

total_area = 2* (length * height + length * breadth  + breadth * height)
print("Total Area of cuboid : " ,total_area)