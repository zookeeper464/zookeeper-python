t = int(input())
answer = []

for _ in range(t):
  n = int(input())
  lst = list(map(int,input().split()))
  visited = [False for  _ in range(n)]
  ans = 0

  for i in range(n):
    if not visited[i]:
      cnt = 0
      turn = dict()
      turn[i] = cnt
      temp = i
      visited[i] = True
      while True:
        temp = lst[temp]-1
        if temp in turn.keys():
          ans += turn[temp]
          break

        elif visited[temp] == True:
          ans += len(turn.keys())
          break

        visited[temp] = True
        cnt += 1
        turn[temp] = cnt

  answer.append(ans)

for ans in answer:
  print(ans)
