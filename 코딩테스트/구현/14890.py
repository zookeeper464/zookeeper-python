n,l = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]

answer = 2*n
for i in range(n):
  temp = lst[i][0]
  idx = 0
  switch = False
  for j in range(1,n):
    if temp == lst[i][j]-1 and j-idx>=l:
      temp = lst[i][j]
      idx = j
    elif temp == lst[i][j]+1:
      if j+l>n:
        answer -= 1
        switch = True
        break
      for k in range(1,l):
        if lst[i][j] != lst[i][j+k]:
          answer -= 1
          switch = True
          break
      if switch:
        break
      else:
        temp = lst[i][j]
        idx = j+l
    elif temp == lst[i][j]:
      pass
    else:
      answer -= 1
      break

  temp = lst[0][i]
  idx = 0
  switch = False
  for j in range(1,n):
    if temp == lst[j][i]-1 and j-idx>=l:
      temp = lst[j][i]
      idx = j
    elif temp == lst[j][i]+1:
      if j+l>n:
        answer -= 1
        switch = True
        break
      for k in range(1,l):
        if lst[j][i] != lst[j+k][i]:
          answer -= 1
          switch = True
          break
      if switch:
        break
      else:
        temp = lst[j][i]
        idx = j+l
    elif temp == lst[j][i]:
      pass
    else:
      answer -= 1
      break

print(answer)
