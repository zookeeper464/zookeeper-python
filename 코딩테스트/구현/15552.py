import sys
input = sys.stdin.readline
n = int(input())
answer = []
for _ in range(n):
  a, b = map(int,input().split())
  answer.append(a+b)

for i in answer:
  print(i)
