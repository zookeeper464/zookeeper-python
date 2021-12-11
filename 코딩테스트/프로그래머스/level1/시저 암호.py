def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ': answer += i
        elif ord(i)<91: answer += chr(65+(ord(i)+n-65)%26)
        else: answer += chr(97+(ord(i)+n-97)%26)    
    return answer