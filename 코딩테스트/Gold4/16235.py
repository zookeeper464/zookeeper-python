# from heapq import heappop, heappush

# n,m,k = map(int,input().split())
# nutrition = [[5]* n for _ in range(n)]
# add_nutrition = [list(map(int,input().split())) for _ in range(n)]
# tree = [[[] for _ in range(n)] for _ in range(n)]
# for _ in range(m):
#   x,y,z = map(int,input().split())
#   tree[x-1][y-1].append(z)

# dr,dc = [1,1,1,0,0,-1,-1,-1],[-1,0,1,-1,1,-1,0,1]

# def spring_summer():
#   for r in range(n):
#     for c in range(n):

#       if tree[r][c]:
#         temp_num = 0
#         temp_list = []
#         for _ in range(len(tree[r][c])):
#           temp = heappop(tree[r][c])
          
#           if temp <= nutrition[r][c]:
#             nutrition[r][c] -= temp
#             temp += 1
#             heappush(temp_list,temp)

#           else:
#             temp_num += temp//2

#         tree[r][c] = temp_list[:]
#         nutrition[r][c] += temp_num

# def fall_winter():
#   for r in range(n):
#     for c in range(n):

#       for num in tree[r][c]:
#         if num >= 5:
#           for i in range(8):
#             nr,nc = r+dr[i],c+dc[i]
#             if 0<=nr<n and 0<=nc<n:
#               heappush(tree[nr][nc],1)

#       nutrition[r][c] += add_nutrition[r][c]

# def check():
#   answer = 0
#   for r in range(n):
#     for c in range(n):
#       answer += len(tree[r][c])

#   return answer

# for i in range(k):
#   spring_summer()
#   fall_winter()
#   print(i+1)
  
# print(check())

################################################ 틀렸습니다. 더 많이 생산합니다. 계속 수정했는데 더 수정을 요구합니다.
from heapq import heappop,heappush

n,m,k = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(n)]
earth = [[5]*n for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]
size = [[[] for _ in range(n)] for _ in range(n)]
dr,dc = [1,1,1,0,0,-1,-1,-1],[1,0,-1,1,-1,1,0,-1]

for _ in range(m):
    x,y,z = map(int,input().split())
    heappush(tree[x-1][y-1],z)
    size[x-1][y-1].append(z//5)

def step():
    step12()
    print(*tree,sep='\n')
    print()
    print(*earth,sep='\n')
    print()
    step3()
    step4()

def step12(): #봄+여름
    for r in range(n):
        for c in range(n):
            lst,temp,cnt,size[r][c] = [],0,earth[r][c],[]
            for i in range(len(tree[r][c])):
                num = heappop(tree[r][c])
                if cnt >= num:
                    cnt -= num
                    heappush(lst,num+1)
                    if (num+1)//5:
                        size[r][c].append((num+1)//5)
                else:
                    temp += num
                    break
            temp += sum(tree[r][c])
            tree[r][c] = lst[:]
            earth[r][c] = cnt+temp//5

def step3(): #가을
    for r in range(n):
        for c in range(n):
            if size[r][c] == []:
                continue
            for s in size[r][c]:
                for i in range(8):
                    nr,nc = r+dr[i],c+dc[i]
                    if 0<=nr<n and 0<=nc<n:
                        heappush(tree[nr][nc],s)
                    

def step4(): #겨울
    for r in range(n):
        for c in range(n):
            earth[r][c] += mat[r][c]

def check():
    answer = 0
    for r in range(n):
        for c in range(n):
            answer += len(tree[r][c])
    
    return answer

for _ in range(k):
    step()

print(check())