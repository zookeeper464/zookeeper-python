import heapq

t = int(input())
answer = []

for i in range(t):
  n = int(input())
  lst = list(map(int,input().split()))
  heapq.heapify(lst)
  temp = 0
  while len(lst)>1:
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)
    temp += (a+b)
    heapq.heappush(lst,a+b)
  answer.append(temp)
  
for i in answer:
  print(i)
