n = int(input())
lst = list(map(int,input().split()))
dp = [[] for _ in range(n)]
m = int(input())
root, answer = [],0

for idx, i in enumerate(lst):
  if i == m or idx == m:
    pass
  elif i == -1: root.append(idx)
  else:
    dp[i].append(idx)

temp = root
while temp:
  t = temp.pop()
  if len(dp[t]) == 0:
    answer += 1
  else:
    temp += dp[t]

print(answer)
#########################################
# n = int(input())
# lst = list(map(int,input().split()))
# s = set([int(input())])

# dp = [[] for _ in range(n)]
# for i in range(n):
#   if set([i,lst[i]])&s == set():
#     dp[lst[i]].append(i)
#   elif lst[i] == -1:
#     pass
#   else:
#     s.add(i)

# answer = sum([1 for i in dp if i==[]])-len(s)
# print(dp)
# print(s)
# print(answer)
