import sys
input=sys.stdin.readline

N,K=map(int,input().split())
val_list=list(range(1,N+1))
result_list=[]

a=val_list.index(K)
for i in range(N):
  result_list.append(str(val_list[a]))
  del val_list[a]
  n=len(val_list)
  if n!=0:
    a=(a+K-1)%n
  else:
    a=0

print("<", end="")
print(", ".join(result_list), end="")
print(">")
