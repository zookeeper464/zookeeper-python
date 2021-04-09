n = int(input())
lst = []
#필요한 변수 입력

for i in range(n):
  x, y = map(int,input().split())
  lst.append([x,y])
lst.sort(key = lambda x : (x[1],x[0]))
#주어진 x,y 값들을 주어진 조건에 맞게 정렬

for i in lst:
  print(" ".join(list(map(str,i))))
