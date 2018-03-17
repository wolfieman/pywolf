filename = input('Enter File: ')
if len(filename) < 1 : filename = 'data/clown.txt'
handle = open(filename)

di = dict()
for line in handle :
  line = line.rstrip()
  words = line.split()
  for word in words :
    # idiom: retrieve/create/update counter
    di[word] = di.get(word, 0) + 1

# print(di)

# find the most common word
largest = -1
the_word = None
for k, v in di.items() :
  if v > largest :
    largest = v
    the_word = k #capture/remember the largest key

print(the_word, largest)