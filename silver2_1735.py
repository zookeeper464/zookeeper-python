a,b=map(int,input().split())
c,d=map(int,input().split())

M=a*d+c*b
N=b*d
gcd=1

def div(m,n):
  global gcd
  if m>n:
    while m>n:
      m-=n
    div(m,n)
  elif n>m:
    while n>m:
      n-=m
    div(m,n)
  else:
    gcd=m

div(M,N)
print(f"{M//gcd} {N//gcd}")
