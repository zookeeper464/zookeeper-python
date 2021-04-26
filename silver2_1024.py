n, l = map(int,input().split())
answer = ["-1"]
for i in range(l,101):
  if (i*(i-1))//2 > n:
    break
  if (n-((i*(i-1))//2))%i==0:
    answer = [str((n-(i*(i-1))//2)//i+j) for j in range(i)]
    break

print(" ".join(answer))
