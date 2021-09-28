lst = [list(map(int,input().split())) for _ in range(3)]
lst += [lst[0]]

temp = 0
for i in range(3):
  temp += lst[i][0]*lst[i+1][1]-lst[i][1]*lst[i+1][0]

if temp>0: print(1)
elif temp<0: print(-1)
else: print(0)
