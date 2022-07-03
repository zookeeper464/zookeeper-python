from sys import stdin

input = stdin.readline


M = int(input())
nums = [0 for _ in range(21)]
answer = []

for i in range(M):
  word = input().rstrip("\n").split(" ")
  if (word[0]=="add"): nums[int(word[1])] = 1
  elif (word[0]=='remove'): nums[int(word[1])] = 0
  elif (word[0]=='check'): print(nums[int(word[1])])
  elif (word[0]=='toggle'): nums[int(word[1])] = (nums[int(word[1])]+1)%2
  elif (word[0]=='all'): nums = [1 for _ in range(21)]
  elif (word[0]=='empty'): nums = [0 for _ in range(21)]
print(*answer,sep='\n')
