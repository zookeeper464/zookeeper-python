n = int(input())
st = set(map(int,input().split()))
m = int(input())
print(*[1 if i in st else 0 for i in list(map(int,input().split()))], sep='\n')
