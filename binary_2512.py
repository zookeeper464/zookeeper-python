import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
dic = Counter(lst)
tlst = dic.items()
m = int(input())
#필요한 변수 입력

start = 0
end = max(lst)
x = True
#사용할 변수 처리

while start <= end:
  mid = (start +end)//2
  answer = 0
  for v, num in tlst:
    answer += min(v,mid)*num
  #주어진 조건에 따라 이진 분할 알고리즘 실행
  
  if answer < m:
    start = mid+1
    #값이 더 작으면 mid를 키운다.
    
  elif answer > m:
    end = mid-1
    #값이 더 크면 mid를 줄인다.
    
  else:
    print(mid)
    x = False
    break
    #값을 찾으면 탈출한다.
    
if x:
  print(end)
  #값을 찾지 못하고 탈출하면 끝부분을 출력한다.
