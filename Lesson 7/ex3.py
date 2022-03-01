def count(word, letterV):
    count = 0
    for letter in word:
        if letter == letterV:
            count = count + 1
    print(count)

count('nnn','n')