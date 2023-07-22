# ________________________________________________Print all Armstrong Number Under 1000______________________________________________
print("All Armstrong Number:")
s=0
for i in range(1,1001):
    n=i
    while(n>0):
        b=n%10
        s=s+(b*b*b)
        n=n//10
    if(s==i):
        print(i)
    s=0