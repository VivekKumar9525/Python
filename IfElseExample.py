age=int(input("Enter Your Age: "))
if age<100 and age>10:
    if(age>18):
        print("You Can Drive")
    elif(age==18):
        print("We will think about you")
    else:
        print("You can not drive")