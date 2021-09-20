from collections import deque

lst = [deque(map(int,list(input()))) for _ in range(4)]
k = int(input())
roll = [list(map(int,input().split())) for _ in range(k)]

def rotate (num,look,dp):
  q = lst[num-1]
  if look == 1:
    temp = q.pop()
    q.appendleft(temp)
  
  else:
    temp = q.popleft()
    q.append(temp)
  lst[num-1] = q

  if num >1 and dp[num-2] != 0:
    dp[num-2] = 0
    rotate(num-1,look*(-1),dp)

  if num < 4 and dp[num-1] != 0:
    temp = dp[num-1]
    dp[num-1] = 0
    rotate(num+1,look*(-1),dp)

for i in range(k):
  dp = [(lst[0][2]+lst[1][6])%2,(lst[1][2]+lst[2][6])%2,(lst[2][2]+lst[3][6])%2]
  rotate(roll[i][0],roll[i][1],dp)

answer = 0
for i in range(4):
  answer += (2**i)*lst[i][0]
print(answer)
