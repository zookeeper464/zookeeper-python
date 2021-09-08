n,m = map(int,input().split())
a = set([input() for _ in range(n)])
b = set([input() for _ in range(m)])
s = a&b
lst = sorted(list(s))
print(len(lst),*lst,sep='\n')
