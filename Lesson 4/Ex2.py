try:
    hrs = float(input('Enter Hours:'))
    rate = float(input('Enter Rate:'))
    if hrs > 40:
        pay1 = 40*rate
        pay2 = (hrs-40)*rate*1.5
        payT = pay1+pay2
        print(payT)
    else:
        payT = hrs*rate
        print(payT)
except:
    print('Error, please enter numeric input')
