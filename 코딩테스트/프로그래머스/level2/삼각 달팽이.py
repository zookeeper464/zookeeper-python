def solution(n):
    mat = [[0]*i for i in range(1,n+1)]
    dx,dy = [0,1,-1],[1,0,-1]
    x,y,d=0,0,0
    
    for num in range(1,n*(n+1)//2+1):
        mat[y][x] = num
        nx,ny=x+dx[d],y+dy[d]
        if 0<=ny<n and 0<=nx<=ny and mat[ny][nx]==0:
            y,x=ny,nx
            
        else:
            d=(d+1)%3
            x,y=x+dx[d],y+dy[d]
            
    return sum(mat,[])