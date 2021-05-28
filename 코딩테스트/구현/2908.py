a,b = input().split()
l1 = int("".join(list(a)[::-1]))
l2 = int("".join(list(b)[::-1]))
print(max(l1,l2))
