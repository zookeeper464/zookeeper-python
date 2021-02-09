N=int(input())
A=list(map(int,input().split()))[0:N]
B=list(map(int,input().split()))[0:N]
val=0

A.sort()
B.sort()
B.reverse()

for i in range(N):
  val+=A[i]*B[i]

print(val)
