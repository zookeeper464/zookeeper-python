import sys
input = sys.stdin.readline

n, m = map(int,input().split())

lst1, lst2 = [], []
for i in range(n):
  lst1.append(input().rstrip())
for i in range(m):
  lst2.append(input().rstrip())

s1 = set(lst1)
s2 = set(lst2)

answer = list(s1&s2)
answer.sort()
print(len(answer))
for i in answer:
  print(i)
