a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
for i in range(1,a+1 or b+1):
    if(a%i==0 and b%i==0):
        hcf=i
print(hcf)