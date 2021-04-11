n = int(input())
lst = list(map(int,input().split()))
lst.sort()

m = int(input())
sol = list(map(int,input().split()))
visited = [0 for i in range(m)]
#필요한 변수들 입력

se = set(lst)
for idx, v in enumerate(sol):
  if {v}&se:
    visited[idx] = 1
#내부에 있는지 집합을 이용하여 판별

for i in visited:
  print(i)
