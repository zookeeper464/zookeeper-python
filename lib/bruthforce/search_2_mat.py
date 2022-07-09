def search_2_mat(i,j):
  global one, zero
  temp = {mat[i][j],mat[i][j+1],mat[i+1][j],mat[i+1][j+1]}
  if temp == {1}:
    return 1
  elif temp == {0}:
    return 0
  else:
    for t in (mat[i][j],mat[i][j+1],mat[i+1][j],mat[i+1][j+1]):
      if t == 1: one += 1
      elif t == 0: zero += 1
    return -1

while (N>1):
  temp_mat = []
  for row in range(0,N,2):
    temp_list = []
    for col in range(0,N,2):
      temp_list.append(search_2_mat(row,col))
    temp_mat.append(temp_list)
  N = N>>1
  mat = [temp_mat[i][:] for i in range(N)]
  
  # 나중에는 재귀함수를 활용한 방식도 나쁘지 않을듯하다.
