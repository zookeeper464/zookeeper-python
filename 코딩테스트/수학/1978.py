plst = [True for i in range(1001)]
plst[0], plst[1] = False, False
for i in range(2,1001):
  if plst[i]:
    j = 2
    while i*j< 1001:
      plst[i*j]=False
      j += 1
      
n, count = int(input()), 0
lst = list(map(int,input().split()))
for i in lst:
  if plst[i]:
    count += 1

print(count)
