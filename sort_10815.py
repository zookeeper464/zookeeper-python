n = int(input())
net = set(map(int,input().split()))
m = int(input())
mst = list(map(int,input().split()))
met = set(mst)
se = net&met
answer = []
#필요한 변수 입력

for i in mst:
  if {i}&se:
    answer.append("1")
  else:
    answer.append("0")
#교집합 안에 존재하면 1추가 아니면 0추가

print(" ".join(answer))
