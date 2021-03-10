N,M=map(int,input().split())
while N!=M:
  if N%M==0:
    N=M
  if N%M==0:
    break
  if N>M:
    while N>M:
      N-=M
  elif N<M:
    while N<M:
      M-=N
for i in range(N):
  print(1,end="")
