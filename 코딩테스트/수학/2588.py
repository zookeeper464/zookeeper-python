n = int(input())
m = input()
a,b,c = map(int,list(m))

a*=n
b*=n
c*=n
print(a)
print(b)
print(c)
print(100*a+10*b+c)
