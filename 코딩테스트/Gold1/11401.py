def power(a, b):
  if b == 0:
    return 1
  if b % 2:
    return ((power(a,b>>1)**2)*a)%p
  else:
    return (power(a,b>>1)**2)%p
    
p = 1000000007
n,k = map(int,input().split())

lst = [0,1]
for i in range(2, n+1):
  lst.append((lst[-1]*i)%p)

a = lst[n]
b = (lst[n-k]*lst[k])%p

print((a*power(b,p-2))%p)
