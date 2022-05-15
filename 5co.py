#question no.5)

x=float(input("Enter the first side of a triangle:"))
y=float(input("Enter the second side of a triangle:"))
z=float(input("Enter the third side of the triangle:"))
if x+y>z and y+z>x and z+x>y:
    print("No")
else:
    print("Yes")
