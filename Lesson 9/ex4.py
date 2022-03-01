wordRecord = []

fname = open('romeo.txt')

for line in fname:
    words = line.split()
    for word in words:
        if wordRecord.count(word) == 0:
            wordRecord.append(word)
        else:
            continue
wordRecord.sort()
print('Total Number of unique words is ', len(wordRecord))
print(wordRecord)