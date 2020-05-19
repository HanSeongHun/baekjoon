a = []
a.append(0)
a.append(1)
N = int(input())
for i in range(1,N):
    temp = a[i] + a[i-1]
    a.append(temp)
p = a.pop()
print(p)