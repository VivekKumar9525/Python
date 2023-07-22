# _______________________________________________________Reverse of a Number______________________________________________
def rev(n):
    r=0
    while(n>0):
        a=n%10
        r=r*10+a
        n=n//10
    return r
n=int(input("Enter a Number: "))
print("Reverse of a given Number=",rev(n))

# _______________________________________________________Reverse of a Number______________________________________________
# def rev(n):
#     r=0
#     while(n!=0):
#         a=n%10
#         r=r*10+a
#         n=n//10
#     return r
# n=int(input("Enter a Number: "))
# s=rev(n)
# print(s)

# _______________________________________________________Reverse of a Number______________________________________________
# n=int(input("Enter a Number: "))
# r=0
# while n!=0:
#     a=n%10
#     r=r*10+a
#     n=n//10
# print("Reverse of Number=",r)