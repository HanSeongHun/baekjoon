N,M = map(int,input().split())
f= []
def mr(boost):
    cart[0] += boost

def md(boost):
    cart[1] += boost
for i in range(1,M):
    line = list(map(int, input().split()))
    f.append(line[0:N+1])

cart =[0,0]
while(True):
    boost = f[cart[0], cart[1]]
    if f[cart[0]+boost,cart[1]] > f[cart[0],cart[1]+boost]:
        mr(boost)
    else:
        md(boost)