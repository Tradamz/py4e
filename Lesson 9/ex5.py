fname = open('mbox-short.txt')
count = 0
for line in fname:
    a = line.split()
    if line.startswith('From:'):
        print(a[1])
        count = count + 1

print('Total number of lines beginning with from are:', count)
