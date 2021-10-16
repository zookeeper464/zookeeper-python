from collections import deque

n,k = map(int,input().split())
visited = [-1]*1000001

def find_num(k):
  answer = [k]
  temp = k
  while temp != n:
    temp = visited[temp]
    answer.append(temp)

  return answer[::-1]

def check (n,k):
  if n>=k:
    return n-k, list(range(n,k-1,-1))
  
  q = deque([n])
  cnt = 0
  while q:
    cnt += 1
    for _ in range(len(q)):
      temp = q.popleft()
      lst = [temp-1,temp+1,2*temp]
      for i in lst:
        if 0<=i<=100000 and visited[i] == -1:
          visited[i] = temp
          if i == k:
            answer = find_num(k)
            return cnt, answer
          q.append(i)

num,answer = check(n,k)
print(num)
print(*answer)
