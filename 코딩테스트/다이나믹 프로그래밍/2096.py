n = int(input())
lst=[list(map(int,input().split())) for _ in range(n)]
mlst = [lst[i][:] for i in range(n)]

for i in range(1,n):
  lst[i][0] += max(lst[i-1][0],lst[i-1][1])
  lst[i][1] += max(lst[i-1])
  lst[i][2] += max(lst[i-1][2],lst[i-1][1])
  mlst[i][0] += min(mlst[i-1][0],mlst[i-1][1])
  mlst[i][1] += min(mlst[i-1])
  mlst[i][2] += min(mlst[i-1][2],mlst[i-1][1])

print(max(lst[-1]),min(mlst[-1]))
