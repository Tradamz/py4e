fname = open('words.txt')

d = dict()
for line in fname:
    words = line.split()
    for word in words:
        d[word] = d.get(word, 0) + 1
print(d)