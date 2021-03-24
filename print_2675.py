n = int(input())
lst = []

for i in range(n):
    s = input()
    m = int(s[0])
    ls = ""
    for j in s[2:]:
        ls += j * m
    lst.append(ls)

for i in lst:
    print(i)
