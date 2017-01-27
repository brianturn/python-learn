import urllib
import json

url = raw_input('Enter url: ')

uh = urllib.urlopen(url).read()

data = json.loads(uh)

print json.dumps(data, indent=4)

comments = data["comments"] 
print len(comments)  

sum = 0
for item in comments: 
  num = item["count"] 
  sum += num 
  
print sum
	