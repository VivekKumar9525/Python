# _______________________________________________Print set of three words in Dictionary_______________________________________
print("Enter Three City Name....")
a=input("Enter First City Name: ")
b=input("Enter Second City Name: ")
c=input("Enter Third City Name: ")
if(a<b<c):
    print(a,b,c)
elif(b<a<c):
    print(b,a,c)
elif(a<c<b):
    print(a,c,b)
elif(c<a<b):
    print(c,a,b)
elif(b<c<a):
    print(b,c,a)
elif(c<b<a):
    print(c,b,a)