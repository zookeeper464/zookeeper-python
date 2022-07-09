from sys import stdin

def input():
  return stdin.readline().rstrip('\n')

def diff(x,y):
  return sums[y]-sums[x-1]

N,M = [int(x) for x in input().split(" ")]
nums = [int(x) for x in input().split(" ")]
sums = [0 for _ in range(N+1)]
for i in range(N):
  sums[i+1] = nums[i]+sums[i]

answer = []
for _ in range(M):
  x,y = [int(i) for i in input().split(" ")]
  answer.append(diff(x,y))

print(*answer,sep="\n")
