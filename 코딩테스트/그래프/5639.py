def postorder(root,end):
  if root>end:
      return

  node=end+1
  for i in range(root+1,end+1):
    if post[root]<post[i]:
      node=i
      break
 
  postorder(root+1,node-1)
  postorder(node,end)
  print(post[root])
 

import sys
sys.setrecursionlimit(10**9)
 
post=[]
count = 0
while count <= 10000:
  try:
    num = int(input())
  except:break
  post.append(num)
  count += 1
 
postorder(0,len(post)-1)
