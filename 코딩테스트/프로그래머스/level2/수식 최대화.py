# def solution(expression):
#     def calcul(ex,l,num):
#         num = int(num)
#         if ex == '-':
#             for i in range(1,len(l)):
#                 num -= int(l[i])
#         elif ex == '+':
#             num = sum(map(int,l))
#         else:
#             for i in range(1,len(l)):
#                 num *= int(l[i])
#         return str(num)
    
#     answer = 0
#     lst = ['+*-','+-*','-*+','-+*','*+-','*-+']
#     dp = []
#     for i in range(6):
#         temp = expression.split(lst[i][0])
#         for a in range(len(temp)):
#             temp[a] = temp[a].split(lst[i][1])
            
#             for b in range(len(temp[a])):
#                 t = temp[a][b].split(lst[i][2])
#                 n = t[0]
#                 temp[a][b] = calcul(lst[i][2],t,n)
#             n = temp[a][0]
#             temp[a] = calcul(lst[i][1],temp[a],n)

#         n = temp[0]
#         ans = calcul(lst[i][0],temp,n)
#         dp.append(abs(int(ans)))
        
#     answer = max(dp)

#     return answer
##############################
def solution(expression):
    lst = ['+*-','+-*','-*+','-+*','*+-','*-+']
    answer = 0
    for k in range(6):
        temp = [f'({i})' for i in expression.split(lst[k][0])]
        
        for a in range(len(temp)):
            temp[a] = [f'({i})' for i in temp[a].split(lst[k][1])]

            for b in range(len(temp[a])):
                temp[a][b] = f'{lst[k][2]}'.join([f'{i}' for i in temp[a][b].split(lst[k][2])])

            temp[a] = f'{lst[k][1]}'.join(temp[a])

        temp = f'{lst[k][0]}'.join(temp)

        t = abs(int(eval(temp)))

        if answer < t:
            answer = t
                
    return answer