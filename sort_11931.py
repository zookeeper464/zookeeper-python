import sys
input = sys.stdin.readline

n = int(input())
lst = []
#필요한 변수 입력

for i in range(n):
  lst.append(int(input()))
#숫자들 저장

lst.sort(reverse = True)
#숫자들 정렬

for i in lst:
  print(i)
