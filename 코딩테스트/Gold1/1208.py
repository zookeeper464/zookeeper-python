def dfs(cnt,lst,idx,temp,dic):
    l = len(lst)
    if cnt==l+1:
        return
    for i in range(idx+1,l):
        dfs(cnt+1,lst,i,temp+lst[i],dic)
    
    if dic.get(temp):
        dic[temp] += 1
    else:
        dic[temp] = 1

n,s = map(int,input().split())
lst = list(map(int,input().split()))
lst1,lst2 = lst[:n//2],lst[n//2:]
        
n1,n2 = len(lst1),len(lst2)
dic1,dic2 = dict(),dict()
dfs(0,lst1,-1,0,dic1)
dfs(0,lst2,-1,0,dic2)

llst1 = sorted(dic1.keys())
llst2 = sorted(dic2.keys(), reverse=True)
answer,idx1,idx2 = 0,0,0
while True:
    if idx1==len(llst1) or idx2==len(llst2):
        break

    if llst1[idx1]+llst2[idx2] == s:
        answer += dic1[llst1[idx1]]*dic2[llst2[idx2]]
        idx2 += 1
    elif llst1[idx1]+llst2[idx2] > s:
        idx2 += 1
    else:
        idx1 += 1
print(llst1,llst2)
print(dic1,dic2)
if s == 0:
    answer -= 1
print(answer)