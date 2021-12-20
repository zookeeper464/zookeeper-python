def solution(n):
    dp = [0,1]
    for i in range(n-1): dp.append((dp[-1]+dp[-2])%1234567)
    answer = dp[-1]
    return answer