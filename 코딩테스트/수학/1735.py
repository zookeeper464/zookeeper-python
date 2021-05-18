from math import gcd
a, b = map(int,input().split())
x, y = map(int,input().split())

g = gcd(a*y+x*b,b*y)
print((a*y+x*b)//g,b*y//g)
