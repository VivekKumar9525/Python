# _______________________________________________________Example of Python JSON______________________________________________
# ________________________________________________Example of Convert from JSON to Python_____________________________________
import json
json_str='{"Name":"Vivek Kumar","Roll No":55,"Course":"MCA","Section":10}'
print(type(json_str))
convert_dict=json.loads(json_str)       #json.loads() Convert for JSON String to Dictionary
print(convert_dict)

#Using python Pretty print JSON
formatted_str=json.dumps(convert_dict,indent=4,sort_keys=True)
print(formatted_str)
#or
# print(json.dumps(convert_dict,indent=4,sort_keys=True))
print(type(convert_dict))

# ________________________________________________Example of Convert from Python to JSON____________________________________________
# import json
# d={"Name":"Vivek Kumar","Roll No":55,"Course":"MCA","Section":10,"Hello":True}
# print(type(d))
# convert_json=json.dumps(d)       #json.dumps() Convert for Dictionary to JSON String
# print(convert_json)
# print(type(convert_json))
