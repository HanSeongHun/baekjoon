score = 0
bonus = 0

N = int(input())
check = input()
for k in range(N):
    if (check[k] == 'O'):
        score += k+1
        score += bonus
        bonus +=1
    else:
        bonus = 0
print(score)