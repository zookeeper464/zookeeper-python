from math import comb
#조합 함수를 부른다.

n, m, k = map(int,input().split())
row = (k-1)//m
col = (k-1)%m
# 행렬의 크기와 지나가야 하는 위치를 받는다.
# 해당 위치를 행렬의 행과 열로 나타낸다.

if k != 0:
  print(comb(row+col, row)*comb(n-row-1+m-col-1, m-col-1))
else:
  print(comb(n+m-2, n-1))
