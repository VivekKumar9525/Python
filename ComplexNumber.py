# _______________________________________________Check b/w Real and Imaginary Part_______________________________________
a=complex(input("Enter a Complex Number: "))
print(a)
print(a.real)
print(a.imag)
if(a.real>a.imag):
    print("Real Part is Greater than Imaginary Part")
else:
    print("Imaginary Part is Greater than Real Part")