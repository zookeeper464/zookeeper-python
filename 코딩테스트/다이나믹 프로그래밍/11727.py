n = int(input())
lst = [1,1]
for _ in range(1,n):
  lst.append((lst[-1]+2*lst[-2])%10007)
print(lst[-1])
