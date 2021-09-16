l,c = map(int,input().split())
lst = sorted(input().split())

def dfs (cnt,idx,temp):
  if cnt == l:
    num = 0
    for i in temp:
      if i in 'aeiou':
        num += 1

    if num>=1 and cnt-num>=2:
      print(*temp,sep='')
    return

  for i in range(idx+1,c):
    temp.append(lst[i])
    dfs(cnt+1,i,temp)
    temp.pop()

dfs(0,-1,[])
