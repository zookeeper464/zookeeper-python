n = int(input())
s = list(input())
m = len(s)
for _ in range(n-1):
  temp = list(input())
  for i in range(m):
    if s[i] != '?' and s[i] != temp[i]:
      s[i] = '?'

print(''.join(s))
