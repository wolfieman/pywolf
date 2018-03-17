string = 'X-DSPAM-Confidence: 0.8475'

colon_pos = string.find(':')

# print(string)
print(colon_pos)

piece = string[colon_pos+1:]
# print(piece)
value =float(piece)
print(value)