import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter url: ')

data = urllib.urlopen(url).read()
print data
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print len(counts)

sum = 0
for num in counts:
	num = int(num.text)
	sum += num
print sum


	