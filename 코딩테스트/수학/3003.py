lst = list(map(int,input().split()))
temp = [1,1,2,2,2,8]
answer = [" " for _ in range(6)]
for i in range(6):
  answer[i] = str(temp[i]-lst[i])

print(" ".join(answer))
