N= int(input())
blocks =[]
can_see = 1
m = 0
for n in range(N):
    blocks.append(int(input()))

low = blocks[N-1]
i = N-1
while(i >= 0):
    if low < blocks[i]:
        can_see +=1
        low = blocks[i]
    i -= 1
print(can_see)
