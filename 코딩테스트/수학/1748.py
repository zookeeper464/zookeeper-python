n = int(input())
m = len(str(n))
answer = 0

for i in range(1,m):
  answer += 9*(10**(i-1))*i

if m > 1:
  answer += (n-int("9"*(m-1)))*m
else:
  answer += n
print(answer)
