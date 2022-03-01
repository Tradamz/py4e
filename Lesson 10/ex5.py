fname = open('mbox-short.txt')
countMax =  None
emailMax = None

countMin = None
emailMin = None

d = dict()
for line in fname:
    if line.startswith('Author:'):
        words = line.strip()
        words = words.split('@')

        print(words)
        word = words[1]
        d[word] = d.get(word, 0) + 1
print(d)
