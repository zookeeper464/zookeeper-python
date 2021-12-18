def solution(m, musicinfos):
    from math import ceil
    
    def change(string):
        ls = []
        for i in range(len(string)-1):
            if string[i+1] == '#': ls.append(chr(ord(string[i])+32))
            elif string[i] == '#': pass
            else: ls.append(string[i])
            
        if string[-1] != '#': ls.append(string[-1])
        return ''.join(ls)

    def set_time(string):
        string = string.split(':')
        return int(string[0])*60+int(string[1])

    answer = [0,24*60,'(None)']
    m = change(m)
    for musicinfo in musicinfos:
        start,end,title,code = musicinfo.split(",")
        start,end = set_time(start),set_time(end)
        t = end-start
        
        if t < answer[0]: continue
        elif t == answer[0] and answer[1]<start: continue

        code = change(code)
        total_code = code*ceil(t/len(code))
        total_code = total_code[:t]
        
        st = set()
        for j in range(len(total_code)):
            if total_code[j] == m[0]: st.add(total_code[j:j+len(m)])
    
        if len(st) == len(st|set([m])):
            answer = [t,start,title]
    
    answer = answer[-1]

    return answer