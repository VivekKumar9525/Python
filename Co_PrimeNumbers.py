n1=int(input("Enter the First Value: "))
n2=int(input("Enter the Second Value: "))
for i in range(1,n1+1 or n2+1):
    if(n1%i==0 and n2%i==0):
        hcf=i
# print("HCF=",hcf)
if(hcf==1):
    print(n1," and ",n2," are Co-Prime Number")
else:
    print(n1," and ",n2," are not Co-Prime Number")