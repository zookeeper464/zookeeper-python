from sys import stdin
input = stdin.readline
N,M = [int(x) for x in input().split(" ")]
temp = dict()
for _ in range(N):
    key,value = input().rstrip("\n").split(" ")
    temp[key] = value

for _ in range(M):
    print(temp[input().rstrip("\n")])
