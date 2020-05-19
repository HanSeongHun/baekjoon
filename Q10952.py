while(1):
    num = input()
    if(num == '0 0'):
        break
    num = num.split()
    result = int(num[0])+ int(num[1])
    print(result)