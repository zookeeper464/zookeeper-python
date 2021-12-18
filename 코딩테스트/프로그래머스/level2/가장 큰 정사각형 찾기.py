def solution(board):
    answer = 0
    n, m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            if (i == 0 or j == 0):
                if answer == 0 and board[i][j] == 1:
                    answer = 1
                    
            elif board[i][j] == 1:
                board[i][j] = 1+min(board[i-1][j],board[i-1][j-1],board[i][j-1])
                answer = max(board[i][j],answer)
                    
    answer *= answer
    return answer