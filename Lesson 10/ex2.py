fname = open('mbox-short.txt')
d = dict()
for line in fname:
    if line.startswith('From '):
        words = line.split()
        word = words[2]
        d[word] = d.get(word, 0) + 1
print(d)
