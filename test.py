import json

data = '''
{
"Transaction_1": {"Name":"Magnolia","Location":"Ayilon male","Amount":289,"Date":"5/5/18"},
"Transaction_2": {"Name":"Landver","Location":"Cinima-city Ramat-hashron","Amount":15,"Date":"15/5/18"},
"Transaction_3": {"Name":"Superfarm","Location":"Shivat-hacochvim male","Amount":199,"Date":"7/5/18"},
"Transaction_4": {"Name":"Ashura","Location":"Afeka tel-aviv","Amount":16,"Date":"25/5/18"},
"Transaction_5": {"Name":"Magnolia","Location":"Ayilon male","Amount":560,"Date":"5/8/18"},
"Transaction_6": {"Name":"Landver","Location":"Cinima-city Ramat-hashron","Amount":50,"Date":"15/7/18"},
"Transaction_7": {"Name":"Superfarm","Location":"Shivat-hacochvim male","Amount":400,"Date":"7/7/18"},
"Transaction_8": {"Name":"Ashura","Location":"Afeka tel-aviv","Amount":40,"Date":"25/8/18"},
"Transaction_9": {"Name":"Magnolia","Location":"Ayilon male","Amount":289,"Date":"5/5/18"},
"Transaction_10": {"Name":"Landver","Location":"Cinima-city Ramat-hashron","Amount":15,"Date":"19/5/18"},
"Transaction_11": {"Name":"Superfarm","Location":"Shivat-hacochvim male","Amount":199,"Date":"8/5/18"},
"Transaction_12": {"Name":"Ashura","Location":"Afeka tel-aviv","Amount":16,"Date":"24/5/18"},
"Transaction_13": {"Name":"Magnolia","Location":"Ayilon male","Amount":240,"Date":"5/9/18"},
"Transaction_14": {"Name":"Landver","Location":"Cinima-city Ramat-hashron","Amount":0,"Date":"14/5/18"},
"Transaction_15": {"Name":"Superfarm","Location":"Shivat-hacochvim male","Amount":199,"Date":"7/5/18"},
"Transaction_16": {"Name":"Ashura","Location":"Afeka tel-aviv","Amount":100,"Date":"25/8/18"},
"Transaction_17": {"Name":"Magnolia","Location":"Ayilon male","Amount":289,"Date":"5/9/18"},
"Transaction_18": {"Name":"Landver","Location":"Cinima-city Ramat-hashron","Amount":15,"Date":"15/7/18"},
"Transaction_19": {"Name":"Superfarm","Location":"Shivat-hacochvim male","Amount":199,"Date":"7/8/18"},
"Transaction_20": {"Name":"Ashura","Location":"Afeka tel-aviv","Amount":16,"Date":"25/11/18"},
"Transaction_21": {"Name":"Magnolia","Location":"Ayilon male","Amount":289,"Date":"5/5/18"},
"Transaction_21": {"Name":"Landver","Location":"Cinima-city Ramat-hashron","Amount":15,"Date":"15/12/18"},
"Transaction_22": {"Name":"Superfarm","Location":"Shivat-hacochvim male","Amount":199,"Date":"7/9/18"},
"Transaction_23": {"Name":"Ashura","Location":"Afeka tel-aviv","Amount":16,"Date":"25/12/18"},
"Transaction_24": {"Name":"Magnolia","Location":"Ayilon male","Amount":20,"Date":"14/6/18"},
"Transaction_25": {"Name":"Ashura","Location":"Afeka tel-aviv","Amount":400,"Date":"11/12/18"}
}'''



obj = json.loads(data)
#print(obj)




#for key, value in obj.items():
#    print(key,value)



#for item in obj:
#    print(str(item))



#list = obj[data]
#print(list[0])

print('- ' * 20)

# Convert back to JSON for nicer printing
print(json.dumps(obj, indent=4))


with open("Transaction-Data", 'w') as f:
    json.dump(obj, f, indent=2)
