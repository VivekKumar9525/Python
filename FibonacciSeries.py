a=0
b=1
n=input("Enter The Number of Element: ")
n=int(n)
print(a,b,end="  ")
for i in range(1,n):
    c=a+b
    a=b
    b=c
    print(c,end="  ")