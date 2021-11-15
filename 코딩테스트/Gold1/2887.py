#from heapq import heappush,heappop

# n = int(input())
# dist = [[0]*n for _ in range(n)]
# lst = [list(map(int,input().split())) for _ in range(n)]
# visited = [0] * n
# answer = 0

# for i in range(n-1):
#   for j in range(i+1,n):
#     temp = min([abs(lst[i][k]-lst[j][k]) for k in range(3)])
#     dist[i][j] = temp
#     dist[j][i] = temp

# q = []
# visited[0], cnt = 1, 1
# for i in range(1,n):
#   heappush(q,[dist[0][i],i])

# while cnt < n:
#   v,idx = heappop(q)
#   if visited[idx]:
#     continue

#   answer += v
#   visited[idx] = 1
#   cnt += 1

#   for i in range(n):
#     if visited[i]:
#       continue

#     heappush(q,[dist[idx][i],i])

# print(answer)
######################################################################## heapq를 활용하여 데이터를 통해 탐색하는 방법은 메모리가 너무 많이 할당된다.
def order(a):
  if a != parent[a]:
    parent[a] = order(parent[a])

  return parent[a]

n = int(input())
parent = [i for i in range(n)]
answer = 0
xl,yl,zl,dp = [],[],[],[]

for i in range(n):
  x,y,z = map(int,input().split())
  xl.append([x,i])
  yl.append([y,i])
  zl.append([z,i])

xl.sort(); yl.sort(); zl.sort()

for i in range(n-1):
  dp.append([xl[i+1][0]-xl[i][0],xl[i][1],xl[i+1][1]])
  dp.append([yl[i+1][0]-yl[i][0],yl[i][1],yl[i+1][1]])
  dp.append([zl[i+1][0]-zl[i][0],zl[i][1],zl[i+1][1]])

dp.sort()

cnt = 0
for v,x,y in dp:
  if cnt == n-1:
    break
    
  px,py = order(x),order(y)
  if px == py:
    continue

  if px > py: parent[px] = py;
  else: parent[py] = px;
  
  answer += v
  cnt += 1

print(answer)
