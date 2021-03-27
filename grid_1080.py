n, m = map(int,input().split())
before_ = []
after_ = []
for i in range(n):
  before_.append(list(input()))
for i in range(n):
  after_.append(list(input()))
answer = 0
#기본 입력값 입력

for i in range(n-2):
  for j in range(m-2):
    if before_[i][j] != after_[i][j]:
      answer += 1
      for x in range(3):
        for y in range(3):
          if before_[i+y][j+x] == "0":
            before_[i+y][j+x] = "1"
          elif before_[i+y][j+x] == "1":
            before_[i+y][j+x] = "0"
#주어진 조건에 맞게 행렬이 다르다면 같도록 함수 설정

x = True
for i in range(n):
  for j in range(m):
    if before_[i][j] != after_[i][j]:
      x = False
      break
  if not x:
    break
#출력 설정

if x:   
  print(answer)
else:
  print(-1)
