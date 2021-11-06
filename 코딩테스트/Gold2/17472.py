from collections import deque
from heapq import heappush,heappop
import sys
inf = sys.maxsize

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]
visited = [[0]*m for _ in range(n)]
q_list = [[]]

def is_check(r,c,num):
  temp_set = set()
  q = deque([[r,c]])
  visited[r][c] = num
  while q:
    tr,tc = q.popleft()
    for i in range(4):
      nr,nc = tr+dr[i],tc+dc[i]
      if 0<=nr<n and 0<=nc<m and visited[nr][nc] == 0:
        if lst[nr][nc] == 1:
          q.append([nr,nc])
          visited[nr][nc] = num
        else:
          temp_set.add((tr,tc))

  return list(temp_set)

def dist(num,r,c,l):
  cnt = 0
  while True:
    r,c,cnt = r+dr[l],c+dc[l],cnt+1

    if not (0<=r<n and 0<=c<m):
      return

    if visited[r][c] == num:
      return
    
    elif visited[r][c] > 0:
      if table[num][visited[r][c]]+1 > cnt > 2:
        table[num][visited[r][c]] = cnt-1
        table[visited[r][c]][num] = cnt-1
        return
      else:
        return

def check(q_lst,num):
  for tr,tc in q_lst:
    for i in range(4):
      nr,nc = tr+dr[i],tc+dc[i]
      if 0<=nr<n and 0<=nc<m and visited[nr][nc] == 0:
        dist(num,tr,tc,i)

cnt = 1
for r in range(n):
  for c in range(m):
    if lst[r][c] == 1 and visited[r][c] == 0:
      temp = is_check(r,c,cnt)
      q_list.append(temp)
      cnt += 1

hq_list = [[] for _ in range(cnt)]
table = [[inf]*cnt for _ in range(cnt)]

for i in range(1,cnt):
  check(q_list[i],i)

for i in range(1,cnt):
  for j in range(1,cnt):
    if table[i][j] == inf:
      continue
    heappush(hq_list[i],[table[i][j],j])

answer = 0
hq_temp = hq_list[1][:]
set_temp = set([1])

while cnt-1 != len(set_temp):
  if hq_temp == []:
    answer = -1
    break

  val,isl = heappop(hq_temp)
  if isl in set_temp:
    continue
  
  answer += val
  set_temp.add(isl)
  for i in hq_list[isl]:
    heappush(hq_temp,i)
    
print(answer)
