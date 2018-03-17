file_handle = open('data/mbox-short.txt')
for line in file_handle:
    line = line.rstrip()
    words = line.split()

    # Guardian in a compound statement
    if len(words) < 3 or words[0] != 'From' : continue
    print(words[2])