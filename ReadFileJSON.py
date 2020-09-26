import json

#read a file

file = open('employee.json','r')
Data = file.read()



# parse
obj = json.loads(Data)

print(str(obj['Name']))
print(str(obj['lastName']))


#print(str(obj['address']))
list = obj['address']
#print(list)
#print(list[0])
#print(len(list))

for i in range(len(list)):
    print("Address of:", i,"is........" )
    print("street:", list[i].get("street"))
    print("city:", list[i].get("city"))
    print("state:", list[i].get("state"))
