from collections import deque
n=int(input())
lst=deque([0,0,0,0,0,0,0,0,0])
for i in range(n):
  a=int(input())
  lst.append(a+max(lst[0],lst[1],lst[2]))
  lst.append(a+max(lst[3],lst[4],lst[5]))
  lst.append(a+max(lst[6],lst[7]))
  for i in range(3):
    lst.popleft()

print(lst)
print(max(lst))
