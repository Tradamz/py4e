x = 'X-DSPAM-Confidence:0.8475'

position = x.find(':')
print(position)

number = float(x[position+1:])

print(number)