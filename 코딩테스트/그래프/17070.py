n = int(input())
lst1 = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
  for j in range(n):
    if lst1[i][j] == 1:
      lst1[i][j] = -1

lst2, lst3 = [], []
for i in range(n):
  lst2.append(lst1[i][:])
  lst3.append(lst1[i][:])

for i in range(1,n):
  if lst1[0][i] != -1:
    lst1[0][i] = 1
  else:
    break

if lst1[-1][-1] < 1:
  print(0)

else:
  for i in range(1,n):
    for j in range(1,n):
      if lst1[i][j]>-1:
        if lst1[i][j-1]>-1:
          lst1[i][j] += lst1[i][j-1]+lst2[i][j-1]

        if lst3[i-1][j]>-1:
          lst3[i][j] += lst3[i-1][j]+lst2[i-1][j]
          
        if lst1[i-1][j-1]>-1 and lst1[i][j-1]>-1 and lst1[i-1][j]>-1:
          lst2[i][j] += lst1[i-1][j-1]+lst2[i-1][j-1]+lst3[i-1][j-1]

  print(lst1[-1][-1]+lst2[-1][-1]+lst3[-1][-1])
