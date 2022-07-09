from sys import stdin

def input():
  return stdin.readline().rstrip('\n')

N = int(input())
nums = [int(x) for x in input().split(' ')]
nums.sort()
num = int(input())
start,end = 0, N-1
answer = 0
while (start<end):
  if (num == nums[start]+nums[end]):
    start+=1
    answer += 1
  elif (num > nums[start]+nums[end]):
    start += 1
  else:
    end -= 1

print(answer)
