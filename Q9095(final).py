a = int(input())
dp =[1]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for k in range(a):
    num = int(input())
    if(num > 3):
        for i in range(4,num+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[num])