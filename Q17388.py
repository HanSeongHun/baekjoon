s,k,h = map(int,input().split())

if((s+k+h) >= 100):
    print('OK')
else:
    n = min(s,k,h)
    if n ==s:
        print('Soongsil')
    elif n == k:
        print('Korea')
    else:
        print('Hanyang')
