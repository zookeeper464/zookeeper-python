n = int(input())
lst = list(map(int,input().split()))
m = max(lst)
answer = (sum(lst)*100/m)/n
print(answer)
