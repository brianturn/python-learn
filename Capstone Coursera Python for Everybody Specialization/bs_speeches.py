import urllib
from BeautifulSoup import *
import re

base_url = 'http://www.americanrhetoric.com/barackobamaspeeches.htm'
html = urllib.urlopen(base_url).read()

soup = BeautifulSoup(html)

a_tags = soup('a')

# create a list of all href links on the base_url
link_list = []
for tag in a_tags:
  name = tag.get('href', None)
  link_list.append(name)

# create a list of relevant path files
path_list = [] 
for i in link_list:
  if re.search('^speeches.+htm', i):
    path = i
    next_url = "http://www.americanrhetoric.com/" + path
    path_list.append(next_url)

# write the text of all font tags with matching criteria to a txt file
 
fhand = open('bs_write.txt', 'wb')   
    
for i in path_list:
  html = urllib.urlopen(i).read()
  soup = BeautifulSoup(html)

  font_tags = soup('font', {'size':'2'}, {'face':'Verdana'})

  for tag in font_tags:
    data = tag.text
    try:
      fhand.write(data)
    except UnicodeEncodeError:
      continue  
    
fhand.close()

