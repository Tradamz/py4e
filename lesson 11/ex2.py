fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        word = time.split(':')
        word = word[0]
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)