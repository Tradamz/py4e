filename = input('Please input file name:')
spamCount = 0
lineCount = 0
sumV = 0

try:
    if filename == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punkd!')
    elif filename != 'na na boo boo':
        file = open(filename)
        for line in file:
            lineCount = lineCount + 1
            if line.startswith('X-DSPAM-Confidence:'):
                pos = line.find(':')
                value = float(line[pos+1:])
                sumV = sumV + value
                spamCount = spamCount + 1
        average = sumV/spamCount
        print('Average: ', average)
except:
    print('File cannot be found',filename)
    exit()