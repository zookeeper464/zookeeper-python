n = int(input())
num = 1
while num*(num+1)//2<n:
  num += 1

temp = n - num*(num-1)//2
num += 1
print(f"{num-temp}/{temp}")
