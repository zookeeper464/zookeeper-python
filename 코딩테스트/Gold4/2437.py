n = int(input())
lst = sorted(list(map(int,input().split())))
temp = 0
for i in range(n):
  if lst[i]<= temp+1:
    temp += lst[i]
  else:
    break

answer = temp+1
print(answer)
