from math import gcd
a, b = map(int,input().split())
x, y = map(int,input().split())

g = gcd(b,y)
print((a*y//g)+(x*b//g),b*y//g)
