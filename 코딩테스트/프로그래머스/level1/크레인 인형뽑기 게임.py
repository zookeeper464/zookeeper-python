from collections import deque

def solution(board, moves):
    new_board = list(zip(*board))
    for idx, r in enumerate(new_board):
        new_board[idx] = deque(r)
        
    answer = 0
    lst = []
    
    for m in moves:
        while new_board[m-1]:
            if new_board[m-1][0] != 0:
                temp = new_board[m-1].popleft()
                if lst and lst[-1] == temp:
                    lst.pop()
                    answer += 2
                    break
                else:
                    lst.append(temp)
                    break
            else:
                new_board[m-1].popleft()
                
    return answer