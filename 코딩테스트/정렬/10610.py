lst = sorted(list(map(int,list(input()))),reverse=True)
print(lst)
if sum(lst)%3==0 and lst[-1]==0:
  print(*lst,sep='')
else:
  print(-1)
