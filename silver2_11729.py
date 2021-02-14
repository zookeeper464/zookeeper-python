K=int(input())
print(2**K-1)

def change (T, N, M):
  if T==1:
    print(f"{N} {M}")
  else:
    a=[1,2,3]
    a.remove(N)
    a.remove(M)
    temp=a[0]
    change(T-1, N, temp)
    print(f"{N} {M}")
    change(T-1, temp, M)

change(K, 1, 3)
