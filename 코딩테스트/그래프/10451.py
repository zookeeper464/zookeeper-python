t = int(input())
answer = []
for _ in range(t):
  n = int(input())
  lst= [0]+list(map(int,input().split()))
  visited = [False for _ in range(n+1)]
  cnt = 0
  for i in range(1,n+1):
    if not visited[i]:
      visited[i] = True
      cnt += 1
      temp = lst[i]
      while True:
        if not visited[temp]:
          visited[temp] = True
          temp = lst[temp]
        else:
          break
  answer.append(cnt)

for i in answer:
  print(i)
