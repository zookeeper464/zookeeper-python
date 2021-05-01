n = int(input())
#입력 처리

lst = [[] for _ in range(n+1)]
lst[1] = [0,0]
#계산에 필요한 저장소 생성

for i in range(2,n+1):
  lst[i] = [lst[i-1][0]+1, i-1]
  if i%2==0 and lst[i][0]>lst[i//2][0]:
    lst[i] = [lst[i//2][0]+1,i//2]
  if i%3==0 and lst[i][0]>lst[i//3][0]:
    lst[i] = [lst[i//3][0]+1,i//3]
  #경우의 수 중에서 가장 단계가 낮은 수 선택
    
print(lst[-1][0])
# 총 변환 횟수 출력

while lst[n][1]>0:
  print(n, end = " ")
  n = lst[n][1]
print(1)
#1까지 나오기 위한 단계 출력
