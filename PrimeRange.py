n1=int(input("Enter the Range1: "))
n2=int(input("Enter the Range2: "))
for n in range(n1,n2):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        print(n,end=" ")