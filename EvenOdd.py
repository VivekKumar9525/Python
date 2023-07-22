n=int(input("Enter a Number: "))
if(n%2)==0:
    print("Even Number")
else:
    print("Odd Number")

# ____________________________________________________Method-2_________________________________________________
# n=int(input("Enter a Number: "))
# a=n%10
# if n==0:
#     print("Given Number is Zero")     
# elif(a==0 or a==2 or a==4 or a==6 or a==8):
#     print(n,"is Even Number")
# else:
#     print(n,"is Odd Number")


# ____________________________________________________Method-2_________________________________________________
n=int(input("Enter a Number: "))
if(n==0):
    print("Zero")
else:
    a=n%10
    if(a==0 or a==2 or a==4 or a==6 or a==8):
        print("Even Number")
    else:
        print("Odd Number")