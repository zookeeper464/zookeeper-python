n = int(input())
min_list = max_list = list(map(int,input().split()))

for i in range(1,n):
  a,b,c = map(int,input().split())
  
  min_list = [a+min(min_list[:2]),b+min(min_list),c+min(min_list[1:])]
  
  max_list = [a+max(max_list[:2]),b+max(max_list),c+max(max_list[1:])]

print(max(max_list),min(min_list))
