text = input('type string')
index = len(text)
while 0 < index:
    letter = text[index-1]
    print(letter)
    index = index - 1
print('end')