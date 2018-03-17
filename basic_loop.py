largest_so_far = -1
print('Before: ', largest_so_far)
for the_number in [9, 41, 12, 3, 74, 15] :
  if the_number > largest_so_far :
    largest_so_far = the_number
  print(largest_so_far, the_number)

print('After: ', largest_so_far)