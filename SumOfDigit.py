n=int(input("Enter The Number: "))
s=0
while(n)!=0:
    m=n%10
    s=s+m
    n=n/10
print(s)

# ___________________________________________________Method2__________________________________________
# n=int(input("Enter a Number: "))
# s=0
# while n!=0:
#     a=n%10
#     s=s+a
#     n=n//10
# print("Sum of Digit=",s)