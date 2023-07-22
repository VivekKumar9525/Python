# ________________________________________________Take Month Value and Display No. Days___________________________________________
m=int(input("Enter a Month Value: "))
if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    print("31 Days in this month value")
elif(m==2):
    print("28/29 Days in this month value")
elif(m==4 or m==6 or m==9 or m==11):
    print("30 Days in this month value")
elif(m==0 or m>12):
    print("Invalid Month Value")