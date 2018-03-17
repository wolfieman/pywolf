count = 0
total = 0.0

while True :
  input_string = input('Enter a number: ')
  if input_string == 'done' :
    break
  try :
    float_value = float(input_string)
  except :
    print('Invalid input')
    continue

  count += 1
  total += float_value

print(total, count, total / count)