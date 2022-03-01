fname = open('mbox-short.txt')
countMax =  None
emailMax = None

countMin = None
emailMin = None

d = dict()
for line in fname:
    if line.startswith('Author:'):
        words = line.split()
        word = words[1]
        d[word] = d.get(word, 0) + 1
for key in d:
    if emailMax == None or d[key] > countMax:
        emailMax = key
        countMax = d[key]
    if emailMin == None or d[key] < countMin:
        emailMin = key
        countMin = d[key]
print('Max:', emailMax, 'Total:', countMax)
print('Min:', emailMin, 'Total:', countMin)