import sys
from collections import Counter
input = sys.stdin.readline
#모듈을 모두 불러옴

def BS_tree(data,M):
  start, end = 0, max(data)
  #data는 dictionary이므로 key값중 가장 큰 값을 받음

  result = 0
  while start <= end:
    total = 0
    mid = max((start+end)//2,1)
    #0이면 에러가 생기므로 0일때를 제외한다.
    
    for x, num in data.items():
      total += (x//mid)*num
    #같은 수들이 많기 때문에 이를 한꺼번에 처리해줌

    if total < M:
      end = mid -1
      #너무 작으면 더 자름

    else:
      result = mid
      start = mid + 1
      #크거나 같다면 mid를 저장하고 start를 변경함
  
  #while문 반복

  return result
  #while문을 탈출했다면 result 제공 어차피 탈출 당시 mid와 같기 때문에 result대신 mid를 사용해도 된다.

n, m = map(int, input().split())
lst = []
for i in range(n):
  lst.append(int(input()))
data = Counter(lst)
print(BS_tree(data,m))
