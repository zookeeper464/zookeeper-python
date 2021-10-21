answer = []
t = int(input())

def check(num):
  nums,cnt = dict(),0
  nums[num] = cnt
  while True:
    num = lst[num]
    if num in nums.keys():
      return nums[num]
    
    if visited[num]:
      return len(nums)
    else:
      visited[num] = True
      cnt += 1
      nums[num] = cnt

for _ in range(t):
  ans = 0
  n = int(input())
  lst = [0]+list(map(int,input().split()))
  visited = [False] * (n+1)

  for i in range(1,n+1):
    if not visited[i]:
      visited[i] = True
      ans += check(i)
  
  answer.append(ans)

print(*answer, sep='\n')
