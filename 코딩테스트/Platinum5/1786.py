t,p = input().rstrip('\n'),input().rstrip('\n')
l = len(p)
dp = [0] * l
answer = []

end_idx = 0
for start_idx in range(1,l):
    while end_idx>0 and p[start_idx] != p[end_idx]:
        end_idx = dp[end_idx-1]

    if p[start_idx] == p[end_idx]:
        end_idx += 1
        dp[start_idx] = end_idx

p_idx = 0
for t_idx in range(len(t)):
    while p_idx > 0 and t[t_idx] != p[p_idx]:
        p_idx = dp[p_idx-1]
    
    if t[t_idx] == p[p_idx]:
        if p_idx == l-1:
            answer.append(t_idx-(l-1)+1)
            p_idx = dp[p_idx]
        else:
            p_idx += 1

print(len(answer))
print(*answer,sep=' ')