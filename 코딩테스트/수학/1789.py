s = int(input())

if s <100:
  i = 1
  cnt = 0

else:  
  i = int(1.4*(s**0.5))
  cnt = i*(i-1)//2

while s>=cnt:
  cnt += i
  i+=1
i-=2

print(i)
