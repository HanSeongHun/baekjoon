def good_day(result):
    g = result[0] * float(change[0]) + result[1] * float(change[2])
    return g
def bad_day(result):
    b = result[0] * float(change[1]) + result[1] * float(change[3])
    return b

N,feel = map(float,input().split())
change = input()
change = change.split()
result = [1,1]

if (feel == 0):
    result = [float(change[0]),float(change[1])]
else:
    result = [float(change[2]),float(change[3])]

for i in range(int(N-1)):
    result = [good_day(result),bad_day(result)]


print('%.0f' %(result[0] * 1000))
print('%.0f' %(result[1] * 1000))