lst = [0 for _ in range(7)]
ls = list(map(int,input().split()))
for i in ls:
  lst[i] += 1

answer = 0
for idx, i in enumerate(lst):
  if i == 3:
    answer += 10000
    answer += idx*1000
    break
  elif i == 2:
    answer += 1000
    answer += idx*100
  elif i == 1:
    answer += 100*idx

print(answer)
