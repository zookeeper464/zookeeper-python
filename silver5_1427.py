N=input()
N_list=list(N)
N=list(map(int,N_list))
N.sort(reverse=True)
for i in N:
  print(i, end="")
print("\n")
