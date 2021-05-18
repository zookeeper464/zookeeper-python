n,m,k = map(int,input().split())
m -= 1
k -= 1
count =0
while m != k:
  m //=2
  k //=2
  count += 1

print(count)
