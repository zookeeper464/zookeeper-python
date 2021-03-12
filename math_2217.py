n=int(input())
lst=[]
for i in range(n):
  a=int(input())
  lst.append(a)
lst.sort()
answer=[]
for i,v in enumerate(lst):
  answer.append((n-i)*v)

print(max(answer))
