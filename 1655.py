import heapq

n = int(input())
max_lst = []
min_lst = []
answer = []
for _ in range(n):
  m = int(input())
  if len(max_lst)==len(min_lst):
    heapq.heappush(max_lst, m)
  else:
    heapq.heappush(min_lst, -m)

  if min_lst and max_lst[0] < -min_lst[0]:
    temp1,temp2 = heapq.heappop(max_lst), heapq.heappop(min_lst)
    heapq.heappush(max_lst,-temp2)
    heapq.heappush(min_lst, -temp1)

  if len(max_lst)==len(min_lst):
    answer.append(-min_lst[0])
  else:
    answer.append(max_lst[0])

for ans in answer:
  print(ans)
