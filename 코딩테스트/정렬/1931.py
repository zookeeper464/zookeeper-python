n = int(input())
lst = sorted([list(map(int,input().split())) for _ in range(n)],key= lambda x : (x[1],x[0]))
temp,answer = 0,0

for i in range(len(lst)):
  if lst[i][0]>=temp:
    temp = lst[i][1]
    answer += 1

print(answer)
