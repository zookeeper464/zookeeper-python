N=int(input())
val_list=[]
for i in range(N):
  weight, height=map(int,input().split())
  val_list.append([weight,height])
rank=N


def compare(val_list):
  for i in range(N):
    rank=1
    for j in range(N):
      if val_list[i][0]<val_list[j][0] and val_list[i][1]<val_list[j][1]:
        rank+=1
    print(rank, end=" ")

compare(val_list)
