import json

#read a file

file = open('employee.json','r')
Data = file.read()


# parse
obj = json.loads(Data)

print(str(obj['firstName']))
print(str(obj['lastName']))
print(str(obj['address']))
