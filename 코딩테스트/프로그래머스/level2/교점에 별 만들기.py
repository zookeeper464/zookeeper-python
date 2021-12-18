def solution(line):
    def solve(eq1, eq2):
        A, B, E = eq1
        C, D, F = eq2
        if A*D == B*C: return None
        
        if (B*F-E*D)%(A*D-B*C)==0 and (E*C-A*F)%(A*D-B*C)==0:
            x,y = (B*F-E*D)//(A*D-B*C), -(E*C-A*F)//(A*D-B*C)
            return [x,y]
        
        return None

    answer = []
    dp = []
    r1,r2,c1,c2 = float('inf'),-float('inf'),float('inf'),-float('inf')
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            s = solve(line[i], line[j])
            if s == None: continue
                
            r1 = min(r1, s[1])
            r2 = max(r2, s[1])
            c1 = min(c1, s[0])
            c2 = max(c2, s[0])
            dp.append(s)
    
    mat = [['.' for i in range(c1,c2+1)] for _ in range(r1,r2+1)]

    for x, y in dp:
        mat[y - r1][x - c1] = '*'

    for i in mat:
        answer.append(''.join(i))
        
    return answer