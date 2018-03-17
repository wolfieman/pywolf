file_handle = open('data/mbox-short.txt')

count = 0
for line in file_handle:
    count += 1
print('Line Count:', count)

file_handle = open('data/mbox-short.txt')
file_input = file_handle.read()
print('Character Count:', len(file_input))

file_handle = open('data/mbox-short.txt')
for line in file_handle :
  if not line.startswith('From:') :
    continue
  print(line.rstrip())

