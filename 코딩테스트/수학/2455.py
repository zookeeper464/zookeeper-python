answer = 0
temp = 0
for i in range(4):
  a, b = map(int,input().split())
  c = b-a
  temp += c
  answer = max(temp,answer)

print(answer)
