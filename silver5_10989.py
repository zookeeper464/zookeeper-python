n = int(input())
cnt = [0 for i in range(10000+1)]
for i in range(n):
  cnt[int(input())] += 1
for i in range(1, 10000+1):
  if cnt[i]!=0:
    for j in range(cnt[i]):
      print(i)
