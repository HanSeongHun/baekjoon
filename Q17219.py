N, M = map(int,input().split())
dic = {}
for i in range(N):
    k, v = input().split()
    dic[k] = v

for j in range(M):
    f = input()
    print(dic[f])