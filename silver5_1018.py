import sys
input=sys.stdin.readline
chess_list=[]

N,K=map(int,input().split())
for i in range(N):
  a=input()
  b=list(a)[:K]
  chess_list.append(b)

chess=[]
for i in range(4):
  chess.append(["B",'W',"B",'W',"B",'W',"B",'W'])
  chess.append(["W","B",'W',"B",'W',"B",'W',"B"])

val_list=[]
for i in range(0,N-7):
  for j in range(0,K-7):
    count=0
    for k in range(8):
      for l in range(8):
        if chess[k][l]==chess_list[i+k][j+l]:
          count+=1
    val_list.append(count)
    val_list.append(64-count)
print(min(val_list))
