num = float(input())

if num == 0:
    print('zero')
elif num > 0:
    if num > 1000000:
        print('large positive')
    elif 1000000 > num > 1:
        print('positive')
    else:
        print('small positive')
elif num < 0:
    if num < - 1000000:
        print('large negative')
    elif - 1000000 < num < -1:
        print('negative')
    else:
        print('small negative')
