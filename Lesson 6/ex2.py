maxN = None
minN = None
numbers = []

# number of elements as input
n = int(input('please enter number of elements:'))

# iterating till the range
for i in range(0, n):
    ele = float(input())

    numbers.append(ele)  # adding the element
print(numbers)

for j in numbers:
    if maxN is None or j > maxN:
        maxN = j
    if minN is None or j < minN:
        minN = j
print('Largest Number:', maxN, 'Smallest Number:', minN)
