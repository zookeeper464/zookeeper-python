def pre_order(in_start, in_end, post_start, post_end):
  global answer
  if(in_start>in_end) or (post_start>post_end):
    return

  parents = post_order[post_end]
  answer.append(parents)
  
  left = position[parents] - in_start
  right = in_end - position[parents]

  pre_order(in_start, in_start+left-1, post_start, post_start+left-1)
  pre_order(in_end-right+1, in_end, post_end-right, post_end-1)

n = int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))

position = [0]*(n+1)
for i in range(n):
  position[in_order[i]] = i

answer = []
pre_order(0, n-1, 0, n-1)

print(*answer)
