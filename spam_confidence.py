# Enter filename
# Open file for Read
# Find colon
# Extract Confidence Value
# Convert Confidence Value to float

file_name = input('Enter the file name: ')

file_handle = open(file_name)

colon_position = len('X-DSPAM-Confidence:')
for line in file_handle :
    if(line.startswith('X-DSPAM-Confidence:')) :
      print('Average Value:\n', float(line[colon_position:].rstrip()))
