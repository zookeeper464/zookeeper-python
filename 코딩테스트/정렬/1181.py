import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(set([input().rstrip() for _ in range(n)])), key=lambda x : (len(x),x))
print(*lst,sep='\n')
