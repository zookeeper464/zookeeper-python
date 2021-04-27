n = int(input())
m = int(input())
lst = [[] for i in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  lst[a].append(b)
  lst[b].append(a)
  #친구관계를 처리하기 위한 형식으로 변형

nset = set(lst[1])
#초청하기 위한 친구들을 집합으로 표현
for i in lst[1]:
  nset = nset|set(lst[i])
  #친구의 친구들 중에서 신랑의 친구를 제외하고 추가

print(len(nset)-1)
