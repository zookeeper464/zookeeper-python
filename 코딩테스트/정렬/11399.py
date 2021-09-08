n = int(input())
lst = sorted(list(map(int,input().split())))
answer = 0
for i in range(n-1):
  answer += lst[i]
  lst[i+1] += lst[i]
print(answer+lst[-1])
