# def solution(s):
#     ls,temp = [],None
#     for i in s[1:-1]:
#         if i == '{':
#             temp = ''
#         elif i =='}':
#             ls.append(set(map(int,temp.split(','))))
#             temp = None
#         elif temp == None:
#             pass
#         else:  
#             temp += i
            
#     lst = sorted(list(ls),key = lambda x : len(x))
#     temp_set = set()
#     answer = []
    
#     for st in lst:
#         num = list(st-temp_set)[0]
#         temp_set = st
#         answer.append(num)
        
#     return answer
#################################################
def solution(s):
    from collections import Counter
    
    lst = [int(i.lstrip('{').rstrip('}')) for i in s.split(',')]
    dic = Counter(lst)
    
    lst = sorted(list(dic.items()), key = lambda x : -x[1])
    answer = [int(lst[i][0]) for i in range(len(lst))]
    
    return answer