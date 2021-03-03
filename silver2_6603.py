import sys

lst=[]
v_lst=[]
while True:
  ls = list(map(int,sys.stdin.readline().split()))
  if ls==[0]:
    break
  v_lst.append(ls[0])
  lst.append(ls[1:])
#v_lst=[7,8]
#lst=[[1,2,3,4,5,6,7],[1,2,3,5,8,13,21,34]]

answer=[0,0,0,0,0,0]

def DFS(start,depth,lst,l,answer):
  if depth==6:
    for i in range(6):
      print(answer[i], end=" ")
    print()
    return
  for i in range(start,l):
    answer[depth]=lst[i]
    DFS(i+1,depth+1,lst,l,answer)

n=len(v_lst)
for i in range(n):
  DFS(0,0,lst[i],v_lst[i],answer)
  print()  
