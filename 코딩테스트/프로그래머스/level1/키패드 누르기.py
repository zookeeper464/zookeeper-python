def solution(numbers, hand):
    answer = ''
    r,l = [2,3],[0,3]
    for i in numbers:
        if i%3 == 1:
            l = [0,i//3]
            answer += 'L'
            continue
            
        elif i%3 == 0 and i//3>0:
            r = [2,i//3-1]
            answer += 'R'
            continue
            
        if i == 0:
            check = [1,3]
        elif i%3==2:
            check = [1,(i-1)//3]
            
        r_check = sum([abs(r[k]-check[k]) for k in range(2)])
        l_check = sum([abs(l[k]-check[k]) for k in range(2)])
        
        if r_check<l_check:
            r = check[:]
            answer += 'R'
        elif r_check == l_check:
            if hand == 'right': r = check[:]; answer += 'R'
            else: l = check[:]; answer += 'L'
        else:
            l = check[:]
            answer += 'L'
            
    return answer