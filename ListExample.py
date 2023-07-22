# _______________________________________________Example of List in User Input______________________________________________
# __________________________________________________Use Like Array in Python______________________________________________
a=[]
n=int(input("Enter The Number of ELement: "))
for i in range(n):
    print(i+1,"No is:",end=" ")
    ele=int(input())
    a.append(ele)
print("Given Element: ",a)


# list1=[5,'vv',7,88,20,'vk',]
# for i in list1:
#     if str(i).isnumeric() and i>6:
#         print(i)

# str=input("Enter The String: ")
# print(str.isalpha())

# __________________________________________________Example of String Slicing__________________________________________
# str="this is python"
# print(str[1:4:1])
# print(str[0:-1:2])
# print(str[::-1])
# print(str[::2])
# print(str[6:])
# print(str[-1])

# ____________________________________________________Find Greatest Number in list________________________________________
# a=[]
# n=int(input("Enter The Number of Element: "))
# for i in range(n):
#     print(i+1,"No:",end=" ")
#     ele=int(input())
#     a.append(ele)
# print(a,end=" ")
# max=a[0]
# for x in a:
#     if max<x:
#         max=x
# print(" ")
# print("Greatest Element among this Element",max)

# _________________________________________________Search a Particular Element___________________________________________
a=[]
n=int(input("Enter The Number of Element: "))
for i in range(n):
    print(i+1,"No:",end=" ")
    ele=int(input())
    a.append(ele)
# print(a,end=" ")
e=int(input("Which No. do you want Search: "))
c=0
for x in a:
    if x==e:
        c=c+1
if c==1:
    print("Yes")
else:
    print("No")


# _______________________________________________________Sort list Element______________________________________________
a=[]
n=int(input("Enter The No. of Element: "))
for i in range(n):
    ele=int(input())
    a.append(ele)
print(a,end=" ")
a.sort()
print(a)

# _______________________________________________Print Index of all element in list__________________________________________
a=[]
n=int(input("Enter The No. of Element: "))
for i in range(n):
    ele=int(input())
    a.append(ele)
    print(a,end=" ")
for x in a:
    i=a.index(x)
    print(i)
# ______________________________________________Print Occurrence of all element in list________________________________________
a=[]
n=int(input("Enter The No. of Element: "))
for i in range(n):
    ele=int(input())
    a.append(ele)
print(a,end=" ")
for x in a:
    c=a.count(x)
    print(c)

# ___________________________________________________Sum of all even & odd Number__________________________________________
l=[]
n=int(input("Enter The No. of Element: "))
for i in range(n):
    print(i+1,"No: ",end="")
    ele=int(input())
    l.append(ele)
print(l,end=" ")
a=0
s=0
for x in l:
    if x%2==0:
        a=a+x
    else:
        s=s+x
print("")
print("Sum of Even No=",a)
print("Sum of Odd No=",s)