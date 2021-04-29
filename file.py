from math import pi
r=float(input("input the radius of the circle:"))
area=pi*r*r
print("The area of the circle with radius"+str(r)+"is:"+str(area))


filename=input("input the filename:")
f_extns=filename.split(".")
print("the extension of the file is:"+repr(f_extns[-1]))
