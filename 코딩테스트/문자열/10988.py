s = input()
n = len(s)//2
answer = 1
for i in range(n):
  if s[i] != s[-i-1]:
    answer = 0
    break

print(answer)
