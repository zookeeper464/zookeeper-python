def solution(n, wires):
    answer = n
    v_list = [[] for _ in range(n+1)]
    for s,e in wires:
        v_list[s].append(e)
        v_list[e].append(s)
    
    for s,e in wires:
        st = set([1])
        stack = [1]
        while stack:
            num = stack.pop()
            for i in v_list[num]:
                if num in (s,e) and i in (s,e): continue
                if i in st: continue
                
                st.add(i)
                stack.append(i)
                
        answer = min(answer,abs(n-2*len(st)))
        
    return answer