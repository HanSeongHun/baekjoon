num = int(input())

if (num%4 == 0):
    if(num % 100 != 0 or num % 400 == 0):
        print('1')
    else:
        print('0')
else:
    print('0')
