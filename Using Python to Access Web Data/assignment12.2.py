import urllib
from BeautifulSoup import *

next_url = raw_input('Enter url:')
position = raw_input('Enter position:')
pos = int(position)

count = raw_input('Enter count:')
count = int(count)

repeat = 0
while repeat < count:
  html = urllib.urlopen(next_url).read()
  soup = BeautifulSoup(html)

  tags = soup('a') #retrieve all of the anchor tags

  name_list = []
  for tag in tags:
    name = tag.get('href', None)
    name_list.append(name)
  next_url = name_list[pos-1]
  repeat = repeat + 1

list = []
for tag in tags:
  name = tag.contents[0]
  list.append(name)
print list[pos-1]
