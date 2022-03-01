numberL = []
while True:
    number = input('Please input Number or done to finish')
    try:
        if number  == 'done':
            break
        number = float(number)
        numberL.append(number)
    except:
        print('not an acceptable input')
print('Max value: ', max(numberL))
print('Min value: ', min(numberL))