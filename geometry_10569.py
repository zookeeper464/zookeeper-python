import sys
input = sys.stdin.readline
#입력

n = int(input())
lst = []
for i in range(n):
  v, e = map(int,input().split())
  lst.append(e+2-v)
  #계산
  
for i in lst:
  print(i)
