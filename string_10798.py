import sys
input = sys.stdin.readline

lst = []
for i in range(5):
  lst.append(input().rstrip())


dp = [[""] * 5 for i in range(15)]
for num, word in enumerate(lst):
  for idx, s in enumerate(word):
    dp[idx][num] = s

for i in dp:
  for j in i:
    print(j, end = "")
