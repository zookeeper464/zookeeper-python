s = input()
n = len(s)
answer = 10
for i in range(1,n):
  if s[i] == s[i-1]:
    answer += 5
  else:
    answer += 10

print(answer)
