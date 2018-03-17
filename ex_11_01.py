import re
handle = open('data/mbox-short.txt')

for line in handle :
  line = line.rstrip()
  if re.search('^From:.+@', line) :
    print(line)