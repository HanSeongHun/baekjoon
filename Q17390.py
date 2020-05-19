def prepix(A):
    n = len(A)
    P = [0] * (n+1)
    for k in range(1,n+1):
       P[k] = P[k-1] + A[k-1]
    return P

def count_total(P, x, y):
    return P[y] - P[x]

N,Q = map(int,input().split())
A = list(map(int, input().split()))
A = sorted(A)
pre = prepix(A)


for _ in range(Q):
    L,R = map(int,input().split())
    result = count_total(pre,L-1,R)
    print(result)
