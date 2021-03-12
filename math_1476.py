e,s,m=map(int,input().split())

n=28*19*13*e+15*19*17*s+15*28*10*m
n=(n-1)%(15*28*19)+1
print(n)

