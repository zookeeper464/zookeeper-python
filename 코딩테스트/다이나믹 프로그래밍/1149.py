n = int(input())
r,g,b=map(int,input().split())
for i in range(n-1):
  x,y,z=map(int,input().split())
  r,g,b = x+min(g,b),y+min(r,b),z+min(r,g)
print(min(r,g,b))
