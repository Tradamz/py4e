try:
    file = open('mbox-short.txt')
    #convert file to string
    inp = file.read()
    upperLine = inp.upper()
    print(upperLine)
except:
    print('File cannot be found')