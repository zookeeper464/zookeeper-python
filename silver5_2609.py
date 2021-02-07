a,b=map(int, input().split())

val=max(a,b)
min_val=0
max_val=0
for i in range(1,val):
  if a%i==0 and b%i==0:
    min_val=i
max_val=int(a*b/min_val)
print(min_val)
print(max_val)
