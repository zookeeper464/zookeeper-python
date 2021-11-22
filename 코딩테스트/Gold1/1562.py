n = int(input())
p = 10**9

def check (n):
    if n < 10:
        return 0
    
    dp = [[[0]* (1<<10) for _ in range(10)] for _ in range(n+1)]
    for i in range(10):
        dp[1][i][1<<i] = 1

    for i in range(2,n+1):
        for j in range(9):
            up,down = 1<<(j+1), 1<<(8-j)
            for k in range(1<<10):
                dp[i][j+1][k|up] += dp[i-1][j][k]
                dp[i][j+1][k|up] %= p
                dp[i][8-j][k|down] += dp[i-1][9-j][k]
                dp[i][8-j][k|down] %= p

    answer = 0
    for j in range(1,10):
        answer += dp[-1][j][-1]
        answer %= p
    
    # t = 0
    # for i in range(1,41):
    #     temp = 0
    #     for j in range(1,10):
    #         temp += dp[i][j]
    #     t += temp%p
    # print(t)

    return answer

print(check(n))