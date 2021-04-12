import sys
input = sys.stdin.readline

n, m = map(int,input().split())
temp = (100*m)//n
start, end = 1, n
#필요한 변수 입력

if temp >= 99:
  print(-1)
  #백분율이 99이상이면 -1 출력
  
else:
  while end >= start:
    mid = (start+end)//2
    #비교하기 위한 mid값 설정
    
    if (100*(m+mid))//(n+mid) > temp:
      answer = mid
      end = mid-1
      #더 커졌다면 작아지기 위한 값 찾기
      
    else:
      start = mid+1
      #더 작아졌다면 커지기 위한 값 찾기
      
  print(answer)
