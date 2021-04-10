n = int(input())
arr = []
#필요한 변수 입력

for _ in range(n):
  a,b,c,d = list(map(str,input().split()))
  arr.append( [a, int(b),int(c),int(d)])
  #이름을 아스키 코드가 아닌 문자로 받아서 정렬할 수 있게 변환하여 저장
  
arr.sort(key = lambda x : (-x[1] , x[2],-x[3],x[0]) )
#조건에 맞게 정렬

for i in arr :
    print(i[0])
