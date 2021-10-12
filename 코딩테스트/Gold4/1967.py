from heapq import heappop, heappush
import sys
INF = sys.maxsize

n = int(input())
e_list = [[] for _ in range(n+1)]
for _ in range(n-1):
  a,b,c = map(int,input().split())
  e_list[a].append([c,b])
  e_list[b].append([c,a])

def end_node (start):
  v_list = [INF]*(n+1)
  v_list[start] = 0
  q = [[0,start]]
  save = [0,0]

  while q:
    val,node = heappop(q)
    for next_val, next_node in e_list[node]:
      if v_list[next_node] > next_val+v_list[node]:
        v_list[next_node] = next_val+v_list[node]
        heappush(q,[v_list[next_node],next_node])
        if save[0] < v_list[next_node]:
          save = [v_list[next_node],next_node]
  
  return save

val,node = end_node(1)
answer,last_node = end_node(node)
print(answer)
