s = input()
n = len(s)
dic = {i:[] for i in range(n)}

def check(start,end):
    if start == 0 or end == n-1:
        return
    
    if s[start-1] == s[end+1]:
        dic[start-1].append(end+1)
        check(start-1,end+1)

def dfs(idx,cnt,lst):
    global answer
    for k in range(idx,n):
        if dic[k] == []:
            continue

        for i in dic[k]:
            lst.append([k,i])
            dfs(i+1,cnt-(i-k),lst)
            lst.pop()

    if cnt < answer:
        answer = cnt

for i in range(n-1):
    if s[i] == s[i+1]:
        dic[i].append(i+1)
        check(i,i+1)

for i in range(n-2):
    if s[i] == s[i+2]:
        dic[i].append(i+2)
        check(i,i+2)

answer = 2500
dfs(0,n,[])
print(answer)
