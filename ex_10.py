# filename = input('Enter File: ')

# c = {'a':10, 'b':1, 'c':22}

# print(sorted( [ (v, k) for k , v in c.items() ], reverse=True ) )

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

# find the most common word
largest = -1
the_word = None
for k, v in di.items() :
  if v > largest :
    largest = v
    the_word = k #capture/remember the largest key

x = sorted(di.items())

temp = list()
for k, v in di.items() :
  new_tuple = (v, k)
  temp.append(new_tuple)

temp = sorted(temp, reverse=True)

for v, k in temp[:5] :
  print(k, v)