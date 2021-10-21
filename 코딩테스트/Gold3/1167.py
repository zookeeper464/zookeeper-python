from heapq import heappop, heappush
import sys
inf = sys.maxsize

v = int(input())
v_list = [[] for _ in range(v+1)]

def check (num):
  nums = [[0,num]]
  values = [inf]* (v+1)
  values[num] = 0

  while nums:
    val,num = heappop(nums)
    for next_val,next_num in v_list[num]:
      if values[next_num] > next_val+val:
        values[next_num] = val+next_val
        heappush(nums,[values[next_num],next_num])
  
  long, node = 0,0
  for num,val in enumerate(values):
    if val != inf and long < val:
      long = val
      node = num

  return long, node

for _ in range(v):
  lst = list(map(int,input().split()))
  start = lst[0]
  for i in range(1,len(lst)-1,2):
    v_list[start].append([lst[i+1],lst[i]])
  
long, num = check(1)
answer, _ = check(num)

print(answer)
