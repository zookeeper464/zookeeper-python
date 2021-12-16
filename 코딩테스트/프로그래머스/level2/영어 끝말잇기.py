def solution(n, words):
    answer = [0,0]
    st = set([words[0]])
    temp = words[0]
    for i in range(1,len(words)):
        if temp[-1] == words[i][0] and words[i] not in st:
            temp = words[i]
            st.add(temp)
            continue
        
        answer = [i%n+1,i//n+1]
        break
        
    return answer