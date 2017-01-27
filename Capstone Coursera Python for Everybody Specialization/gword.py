import string

file = open('bs_write.txt')
text = file.read().decode('utf-8')

s = text.replace('&rsquo;', '').replace(',', ' ').replace('.', ' ').replace('\'', '').replace(':', ' ').replace('Book/CDs by Michael E. Eidenmuller, Published by McGraw-Hill (2008)', ' ').replace('&nbsp;', ' ')

words = s.split()

# Adds word to dictionary if length is 5 or more characters
counts = {}
for word in words:
  word = word.lower()
  word = word.strip()
  if len(word) < 5 : continue
  counts[word] = counts.get(word, 0) + 1
  
# Find the top 100 words
words = sorted(counts, key=counts.get, reverse=True)
highest = None
lowest = None
for w in words[:100]:
  if highest is None or highest < counts[w] :
    highest = counts[w]
  if lowest is None or lowest > counts[w] :
    lowest = counts[w]
print 'Range of counts:',highest,lowest


# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('gword.js','w')
fhand.write("gword = [")
first = True
for k in words[:100]:
  if not first : fhand.write( ",\n")
  first = False
  size = counts[k]
  size = (size - lowest) / float(highest - lowest)
  size = int((size * bigsize) + smallsize)
  try:
    fhand.write("{text: '"+k+"', size: "+str(size)+"}")
  except UnicodeEncodeError: continue
fhand.write( "\n];\n")

# Displays the top 100 words:counts in terminal  
lst = []
for k, v in counts.items():
  lst.append((v, k))
   
lst.sort(reverse=True)

for k,v in lst[:100]:
  print v, k 

print "Output written to gword.js"
print "Open gword.htm in a browser to view"	     
