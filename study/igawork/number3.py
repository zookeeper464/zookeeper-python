# number 3
# 주어진 데이터에 대해서 변수를 설정해준다.
# 주어진 데이터 : prison, 세로 길이 : n, 가로 길이 : m
prison = [[0,1,0,1,0,1,0,1],[0,0,0,0,0,1,0,0],[1,0,1,0,0,1,0,1],[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,1],[0,1,0,0,0,0,0,0],[0,0,0,0,1,0,1,0]]
n, m = len(prison),len(prison[0])

# dfs탐색을 통해 가장 많이 저장된 수용인원을 저장한다.

# 빈 자리에 대한 변수를 설정하고 해당 데이터에 대해서 서로 공존 할 수 없는 장소를 그래프로 설정한다.
# 해당 설정을 통해 반복적인 탐색시간을 줄일 수 있다.
# 빈칸의 주소 : zeros, 빈칸의 개수 : z, 빈칸의 주소에 대한 인덱스 dic, 바라보는 시각에 따른 변수 : dr,dc, 시각을 공유하는 죄수들 : v_list
zeros = []
for r in range(n):
  for c in range(m):
    if prison[r][c] == 0:
      zeros.append([r,c])
z = len(zeros)
dic = {f'{zeros[i]}':i for i in range(z)}
dr,dc = [1,-1,0,0],[0,0,1,-1]
v_list = [[] for _ in range(z)]

# 데이터를 찾는데 index를 활용하면 너무 오래걸리고 반복되는 작업이 많기 때문에 dictionary를 통해 탐색시간을 줄인다.
# dictionary의 key는 list가 올 수 없으므로 해당 데이터를 string의 형태로 key를 설정한다.
for i in range(z):
  r,c = zeros[i]
  for j in range(4):
    nr,nc = r+dr[j],c+dc[j]
    while 0<=nr<n and 0<=nc<m:
      if prison[nr][nc] == 0:
        v_list[i].append(dic[f'{[nr,nc]}'])
        nr += dr[j]
        nc += dc[j]
      else:
        break

# dfs를 통해 가장 많이 저장된 값을 X, 그리고 경우의 수를 Y로 설정하여 저장한다.
def dfs(idx,lst,visited):
  global X,Y
  for i in range(idx+1,z):
    # 공존할 수 없는 데이터가 아니라면 다음 탐색을 진행한다.
    if not visited[i]:
      lst.append(i)
      visited[i] = True
      # visited는 다른 탐색에 쓰이기 때문에 deepcopy를 통해 새로운 리스트를 생성하고 이를 다시 탐색에 활용한다.
      temp = visited[:]
      for j in v_list[i]:
        temp[j] = True

      dfs(i,lst,temp)

      # 탐색이 마무리 되었다면 해당 탐색에 대한 뒷정리를 한다.
      lst.pop()
      visited[i] = False
  
  # 작업이 모두 마쳤을 때, 해당 리스트에 대해서 X와 비교하여 길이가 크다면 X, Y를 재설정하고 X와 같다면 Y의 개수를 하나 늘려준다.
  l = len(lst)
  if X < l:
    X = l
    Y = 1
    print(X)
  elif X == l:
    Y += 1

X,Y = 0,0
dfs(-1,[],[False]*z)

print(f'최대 {X} 명, {Y} 가지')
