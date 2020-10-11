import json
import requests



payload = {"id": "21213"}
r = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population",params=payload)

print(r.url)
print(r.text)




#print(json.dumps(data, indent=4))
#with open("US-info", 'w') as f:
#    f.write(r)
#print(r)
#print(r.text)
#print(r.headers)
