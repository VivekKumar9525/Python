import os
import math
while(True):
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multipication")
    print("4. Division")
    print("5. Mudulus")
    print("6. Factorial")
    print("7. Exit....")
    print("Enter Your Choice:",end=" ")
    ch=int(input())
    match(ch):
        case 1:
            print("Enter First Value:",end=" ")
            a=float(input())
            print("Enter Second Value:",end=" ")
            b=float(input())
            c=a+b
            print("Sum=",c)
        case 2:
            print("Enter First Value:",end=" ")
            a=float(input())
            print("Enter Second Value:",end=" ")
            b=float(input())
            c=a-b
            print("Sub=",c)
        case 3:
            print("Enter First Value:",end=" ")
            a=float(input())
            print("Enter Second Value:",end=" ")
            b=float(input())
            c=a*b
            print("Multi=",c)
        case 4:
            print("Enter First Value:",end=" ")
            a=float(input())
            print("Enter Second Value:",end=" ")
            b=float(input())
            c=(a/b)
            print("Div=","%.2f"%c)
        case 5:
            print("Enter First Value:",end=" ")
            a=float(input())
            print("Enter Second Value:",end=" ")
            b=float(input())
            c=a%b
            print("Mod=",c)
        case 6:
             f=1
             print("Enter The Value:",end=" ")
             a=int(input())
             for i in range(1,a+1):
                 f=f*i
             print("Factorial=",f)
        case 7:
            break
        case _:
            print("Invalid Input!!!!")    
os.system('cls')