
import json
import requests

r = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")

pack_json = r.json()

#print(pack_json)


pack_str = json.dumps(pack_json, indent=2)
print(pack_str)
#for key, value in pack_json.items():
#    print(key, value)

#print(type(pack_str))





#print(len(pack_str))
