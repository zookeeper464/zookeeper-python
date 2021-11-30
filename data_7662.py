from heapq import heappop,heappush
t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    dic,m,M,num = dict(),[],[],0
    for _ in range(n):
        a,b = input().split()
        b = int(b)
        if a == 'I':
            heappush(m,b)
            heappush(M,-b)
            if dic.get(b): dic[b] += 1
            else: dic[b] = 1
            num += 1
        else:
            if num == 0:
                continue

            if b == 1:
                while M:
                    x = -heappop(M)
                    if x in dic:
                        num -= 1
                        dic[x] -= 1
                        if dic[x] == 0:
                            del(dic[x])
                        break

            else:
                while m:
                    x = heappop(m)
                    if x in dic:
                        num -= 1
                        dic[x] -= 1
                        if dic[x] == 0:
                            del(dic[x])
                        break
            if num == 0:
                m,M,dic = [],[],dict()
                
        print(num,dic,m,M)

    lst = sorted(list(dic))
    if lst:
        answer.append(f'{lst[-1]} {lst[0]}')
    else:
        answer.append('EMPTY')

print(*answer,sep='\n')