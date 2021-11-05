def f(n, s):
  global answer
  if s==0:
    if answer > n:
      answer = n
    return
  elif n>=answer:
    return
  
  for i in range(10):
    for j in range(10):
      if lst[i][j]==0 or visited[i][j]==1:
        continue

      for k in range(5, 0, -1):
        if not (paper[k]>0 and i+k<=10 and j+k<=10): 
          continue

        cover = 0
        for r in range(i,i+k):
          for c in range(j, j+k):
            if visited[r][c]==0:
              cover += lst[r][c]
              
        if cover!=(k*k):
          continue
        
        for r in range(i, i + k):
          for c in range(j, j + k):
            visited[r][c] = 1
        paper[k] -= 1

        f(n+1, s-k*k)
        for r in range(i, i + k):
          for c in range(j, j + k):
            visited[r][c] = 0
        paper[k] += 1

      return

lst = [list(map(int, input().split()))for _ in range(10)]
visited = [[0]*10 for _ in range(10)]
answer = 26
ones = 0
paper = [0, 5, 5, 5, 5, 5]
for i in range(10):
  for j in range(10):
    if lst[i][j]==1:
      ones += 1

f(0, ones)
print(answer if answer != 26 else -1)
