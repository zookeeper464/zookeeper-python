from collections import deque

t = int(input())
answer = []

p_list = [1]*10000
p_list[0],p_list[1] = 0,0
for i in range(2,10000):
  if p_list[i]:
    for j in range(2,10000//i+1):
      if i*j>=10000:
        break
      p_list[i*j] = 0

def check (a,b):
  visited = [p_list[i] for i in range(10000)]

  if a == b:
    return 0
  
  cnt = 0
  q = deque([a])
  visited[int(a)] = 0
  size = [1000,100,10,1]
  
  while q:
    cnt += 1
    for _ in range(len(q)):
      temp = q.popleft()
      num = int(temp)
      for i in range(4):
        next_num = num - (int(temp[i])*size[i])
        for j in range(10):
          if next_num == int(b):
            return cnt

          if visited[next_num] and next_num>999:
            visited[next_num] = 0
            q.append(str(next_num))
            
          next_num += size[i]
          
for _ in range(t):
  a,b = input().split()
  answer.append(check(a,b))

print(*answer,sep='\n')
