n, k = map(int,input().split())
lst = [i for i in range(1,n+1)]
answer = []

a=k-1
for _ in range(n):
  answer.append(str(lst[a]))
  del lst[a]
  l=len(lst)
  if l!=0:
    a = (a+k-1)%l
  else:
    a=0

print("<",end="")
print(", ".join(answer),end="")
print(">")
