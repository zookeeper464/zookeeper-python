s = input()
lst = sorted([s[i:] for i in range(len(s))])
print(*lst,sep='\n')
