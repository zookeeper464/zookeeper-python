from math import log

def change(num,diff):
  pass

def sum_all(start,end):
  pass

n,m,k = map(int,input().split())
lst = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)
answer = []
for i in range(int(log(n,2))+1):
  for j in range(2**i,n+1,2**(i+1)):
    dp[j] = sum(lst[j-2**i+1:j+1])

for _ in range(m+k):
  a,b,c = map(int,input().split())
  if a == 1:
    diff = c - lst[b]
    change(b,diff)

  else:
    temp = sum_all(b,c)
    answer.append(temp)

print(*answer,sep='\n')
# 변환하는 과정을 어떻게 구현할것인가? - 다음 탐색해야 하는 숫자를 가져온다.
# 더하는 과정을 어떻게 구현할것인가? - 현재 탐색하는 노드와 트리의 범위에 대해서 저장된 범위의 차이를 구하고 해당 차이만큼 함수를 실행한다. 같다면 값을 리턴한다.
# 함수를 구현해보자.
######################################################################################################
# def init(node, start, end):
#   if start == end :
#     tree[node] = l[start]
#     return tree[node]

#   else :
#     tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
#     return tree[node]
 
# def subSum(node, start, end, left, right) : 
#   if left > end or right < start :
#     return 0

#   if left <= start and end <= right :
#     return tree[node]

#   return subSum(node*2, start, (start+end)//2, left, right) + subSum(node*2 + 1, (start+end)//2+1, end, left, right)
 
# def update(node, start, end, index, diff) :
#   if index < start or index > end :
#     return

#   tree[node] += diff
#   if start != end :
#     update(node*2, start, (start+end)//2, index, diff)
#     update(node*2+1, (start+end)//2+1, end, index, diff)
 
 
# n, m, k = map(int, input().rstrip().split())
# l,answer = [int(input()) for _ in range(n)],[]
# tree = [0] * 3000000
 
# init(1, 0, n-1)
# for _ in range(m+k) :
#   a, b, c = map(int, input().rstrip().split())
#   if a == 1 :
#     b = b-1
#     diff = c - l[b]
#     l[b] = c
#     update(1, 0, n-1, b, diff)
#   elif a == 2 :                
#     answer.append(subSum(1, 0, n-1 ,b-1, c-1))

# print(*answer,sep='\n')
