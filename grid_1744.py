n = int(input())
lst = []
for i in range(n):
  lst.append(int(input()))
#필요한 입력값 입력

answer = 0
plst = []
mlst = []
for i in lst:
  if i > 1 :
    plst.append(i)
  elif i == 1:
    answer += 1
  else:
    mlst.append(i)
plst.sort(reverse =True)
mlst.sort()
#계산에 필요한 입력값들 리스트 처리

nplus = len(plst)
nminus = len(mlst)
#변수 설정



for i in range(nplus//2):
  answer += plst[2*i] * plst[2*i+1]
if nplus % 2 == 1:
  answer += plst[-1]
#플러스 부분 함수 처리
for i in range(nminus//2):
  answer += mlst[2*i] * mlst[2*i+1]
if nminus % 2 == 1:
  answer += mlst[-1]
#마이너스 부분 함수 처리

print(answer)
