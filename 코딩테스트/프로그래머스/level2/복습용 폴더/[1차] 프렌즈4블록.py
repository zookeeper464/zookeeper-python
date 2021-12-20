def solution(m, n, board):
    def check(mat,visit):
        new_mat = [[] for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(len(mat[i])):
                if visit[i][j] == 1: ans += 1
                else: new_mat[i].append(mat[i][j])
        
        return ans,new_mat
                    
    answer = 0
    board = list(zip(*board))
    board = [list(i)[::-1] for i in board]
    
    while True:
        visited = [[0 for _ in range(len(board[i]))] for i in range(n)]
        for r in range(n-1):
            for c in range(len(board[r])-1):
                if visited[r][c] == -1: continue
                    
                if board[r][c] == board[r][c+1]:
                    if len(board[r+1])<=c+1: continue
                    if board[r][c] != board[r+1][c]: continue
                        
                    if board[r+1][c] == board[r+1][c+1]:
                        for i in range(2):
                            for j in range(2):
                                visited[r+i][c+j] = 1
                    else:
                        if visited[r+1][c]: continue
                        visited[r+1][c] = -1
    
        num,board = check(board,visited)
        if num: answer += num
        else: break
            
    return answer