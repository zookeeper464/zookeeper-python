import sys
input = sys.stdin.readline

def fx (lst):
  for i in range(len(lst)-1):
    if lst[i] == lst[i+1][0:len(lst[i])]:
      return "NO"
  return "YES"
#lst가 정렬된 상태로 주어졌다면 앞뒤 번호만 비교하면 된다.

t = int(input())
answer = []

for idx in range(t):
  lst = []
  n = int(input())

  for i in range(n):
    lst.append(input().rstrip())
  lst.sort()
  #입력이 필요한 값 입력, 정렬
  answer.append(fx(lst))
  #함수 호출

for i in answer:
  print(i)
