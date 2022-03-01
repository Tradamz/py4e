fname = open('mbox-short.txt')
d = dict()
for line in fname:
    if line.startswith('Author:'):
        words = line.split()
        word = words[1]
        d[word] = d.get(word, 0) + 1
print(d)