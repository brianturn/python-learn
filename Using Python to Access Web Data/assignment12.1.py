import urllib
from BeautifulSoup import *

url = raw_input('Enter url:')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

#retrieve all of the anchor tags
tags = soup('span')

numlist = []
for tag in tags:
  content = int(tag.contents[0])
  numlist.append(content)
  sum_list = sum(numlist)
print sum_list