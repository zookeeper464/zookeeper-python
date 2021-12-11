def solution(phone_number):
    answer=''.join(['*' if i<-4 else phone_number[i] for i in range(-len(phone_number),0)])
    return answer