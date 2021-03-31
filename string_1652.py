n = int(input())

lst = []
dp = ["" for i in range(n)]
answer1 = 0
answer2 = 0
for i in range(n):
  s = input()
  for j in range(n):
    dp[j] += s[j]
  l = s.split("X")
  for j in l:
    if len(j) >= 2:
      answer1 += 1
  #입력하고자하는 값을 입력한다.
  #가로로 세야하는 부분을 split을 통해 구분하고 더한다.
  #세로로 세야 하는 부분을 따로 리스트를 구한다.

for i in dp:
  l = i.split("X")
  for j in l:
    if len(j) >= 2:
      answer2 += 1
  #세로로 세야 하는 부분을 split을 통해 구분하고 더한다.

print(answer1, answer2)
