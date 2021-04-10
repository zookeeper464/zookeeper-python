n, m = map(int,input().split())
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
#필요한 변수 입력

lst = lst1+lst2
lst.sort()
#정렬

print(" ".join(list(map(str,lst))))
