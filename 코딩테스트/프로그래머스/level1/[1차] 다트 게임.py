def solution(dartResult):
    num,stack = '',[]
    for i in dartResult:
        if 48<=ord(i)<58:
            if type(num) == int:
                num = ''
            num += i
        else:
            num = int(num)
            for idx,j in enumerate('SDT'):
                if j==i: stack.append(num**(idx+1))
            if i == '#': stack[-1] *= -1
            elif i == '*':
                if len(stack)>1: stack[-2] *= 2
                stack[-1] *= 2
                
    answer = sum(stack)
    
    return answer