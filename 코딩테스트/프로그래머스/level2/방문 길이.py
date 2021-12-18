def solution(dirs):
    answer = 0
    idx,d,dr,dc = [5,5],{'U':2,"D":0,"R":1,"L":3},[1,0,-1,0],[0,1,0,-1]
    mat = [[[0,0,0,0] for _ in range(11)] for _ in range(11)]
    
    for i in dirs:
        (r,c),j = idx,d[i]
        tr,tc = r+dr[j],c+dc[j]
        
        if 0<=tr<11 and 0<=tc<11:
            if mat[r][c][j] == 0:
                mat[r][c][j], mat[tr][tc][(j+2)%4] = 1,1
                answer += 1
            idx = [tr,tc]
    return answer