# _______________________________________________Check Nature of roots of Quadratic Equation_______________________________________
from math import sqrt
a=int(input("Enter the Value of a: "))
b=int(input("Enter the Value of b: "))
c=int(input("Enter the Value of c: "))
d=(b*b)-4*a*c
if(d>0):
    root1=-b+sqrt(d)/2*a
    root2=-b-sqrt(d)/2*a
    print("Root1=",root1," and Root2=",root2)
    print("roots are real and distinct (unequal)")
elif(d==0):
    root1=root2=-b/2*a
    print("Root1 and Root2: ",root1)
    print("roots are real and equal")
elif(d<0):
    print("roots are real and imaginary")