import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dic1 = {}
dic = {}

for i in range(n):
  temp = input().rstrip()
  dic1[i+1] = temp
  dic[temp] = i+1
#입력 해야 하는 값 입력

answer = []
for i in range(m):
  temp = input().rstrip()
  try:
    x = dic1[int(temp)]
    #숫자를 주면 해당하는 포켓몬 출력
  except:
    x = dic[temp]
    #포켓몬을 주면 해당하는 번호를 찾아 출력
  answer.append(x)

for i in answer:
  print(i)
