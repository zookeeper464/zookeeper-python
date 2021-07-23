s, n = input().split()
n = int(n)
answer = 0
m = len(s)
for i in range(m):
  temp = ord(s[m-i-1])
  if temp>60:
    temp -= 55
  else:
    temp -= 48
  answer += temp*(n**i) 

print(answer)
