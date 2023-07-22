# _______________________________________________________Example of Python Dictionary______________________________________________
# dict={"Name":"Vivek","College":"Galgotias","Course":"MCA","Addmission Number":"22SCSE2030629"}
# print(dict)
# for key, value in dict.items():
#     print(key, " : ",value) 
# for key in dict:
#     print(key," : ",dict[key])
# print(len(dict))
# for i in dict:
#     print(i)
# print(dict.values())

# _______________________________________________________dict items each in one lines______________________________________________
# d={"krishna":26,"vivek":22,"adarsh":20}
# print(d)
# for key, value in d.items():
#     print(key, " : ",value)

# _______________________________________________________dict items each in one lines______________________________________________
# d={70:"vivek",50:"ajit",10:"Aditya",40:"saransh"}
# for key, value in d.items():
    # print(key," : ",value)

# _______________________________________________________sort dict according to key______________________________________________
# d={"Name":"Vivek","Roll":70,"Class":"MCA","Section":10}
# for key, value in sorted(d.items()):
#     print(key," : ",value)

# _______________________________________________________sort dict according to value______________________________________________
# d={"one":5,"two":7,"three":2,"four":4}
# sd=sorted(d.values())
# print(sd)

# import json
# d=input("Enter a Dictionary: ")
# d=dict(json.loads(d))
# s= s(d.values())
# print(s)

# _______________________________________________________sum of dict value______________________________________________
from ast import literal_eval
d = literal_eval(input('Enter a dictionary'))
s = 0
for i in d.values():
    s +=i
print(s)