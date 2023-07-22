# _______________________________________________________Check Leap Year or Not______________________________________________
year=int(input("Enter The Year: "))
if(year%100)==0:
    if (year%400)==0:
        print("Leap Year")
    else:
         print("Not a Leap Year")
else:
    if(year%4==0):
        print("Leap Year")
    else:
         print("Not a Leap Year")

         # _______________________________________________________Check Leap Year or Not______________________________________________
# y=int(input("Enter a Year:"))
# if(y%100==0):
#     if(y%400==0):
#         print("Leap Year")
#     else:
#         print("Not a Leap Year")
# elif(y%4==0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")