# ___________________________________________________len() Function__________________________________________
# s1=input("Enter The String: ")
# l=len(s1)
# print("Length of String=",l)


# ___________________________________________________index() Function__________________________________________
# s1="Hello"
# print(s1.index('o'))


# ___________________________________________________count() Function__________________________________________
# s1="Good Morning"
# print(s1.count('o'))


# ___________________________________________________Reverse String__________________________________________
# s1="Good Morning"
# print(s1[::-1])


# ___________________________________________________Occurrence Character__________________________________________
# s1=input("Enter The String: ")
# c1=input("Enter a Character: ")
# c=0
# for i in s1:
#     if i==c1:
#         c=c+1
# print(c)

# ___________________________________________________Count Vowels in String__________________________________________
# s1=input("Enter the String:")
# c=0
# for x in s1:
#     if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
#         c=c+1
# print(c)

# ___________________________________________________Count Words in String__________________________________________
# s=input("Enter The String: ")
# tw=len(s.split())
# print("Total Words=",tw)


# ___________________________________________________Arrange word in alphabetical order________________________________
# s=input("Enter The String: ") 
# w=s.split()
# w.sort()
# for i in w:
#     print(i)


# ___________________________________________________Check String Palindrome or not__________________________________________
# s=input("Enter The String: ")
# if s[::1]==s[::-1]:
#     print("yes")
# else:
#     print("no")


# ___________________________________________________Check String Palindrome or not__________________________________________
# s=input("Enter The String: ")
# a=[]
# for i in j:
#     if i not in a:
#         a.append(i)
# for x in range(0,len(a)):
#     print(a[x])


# ___________________________________________________Remove duplicate character of string__________________________________________
# from collections import OrderedDict
# def solve(s):
#    d = OrderedDict()
#    for c in s:
#       if c not in d:
#          d[c] = 0
#       d[c] += 1
#    return ''.join(d.keys())
# s = "bbabcaaccdbaabababc"
# print(solve(s))


# ___________________________________________________Search Pattern in String__________________________________________
# import  re
# patt='^a..s$'
# s='ayys'
# res=re.match(patt,s)
# if res:
#     print("Yes")
# else:
#     print("No")


# ___________________________________________________Count Pattern in String__________________________________________
import re
s = 'ab ab ab aba'
res= len(re.findall('(?=(aba))', s)) 
print("Number of substrings", res)