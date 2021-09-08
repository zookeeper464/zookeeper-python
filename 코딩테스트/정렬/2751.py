n = int(input())
lst = sorted([int(input()) for _ in range(n)])
print(*lst,sep='\n')
