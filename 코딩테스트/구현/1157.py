s = input().upper()
#65
dp = [0 for _ in range(26)]
for i in s:
  dp[ord(i)-65] += 1

answer = "?"
num = 0
for idx, v in enumerate(dp):
  if num<v:
    num = v
    answer = chr(idx+65)
  elif num==v:
    answer = "?"

print(answer)
