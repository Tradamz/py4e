total = 0
count = 0
average = 0

while True:
    try:
        number = input('please submit number:')
        if number == 'done':
            print('done', 'Total:', total, 'Count:', count, 'Average:', average)
            break
        number = float(number)
        count = count + 1
        total = total + number
        average = total/count
    except:
        print('error poor input')
