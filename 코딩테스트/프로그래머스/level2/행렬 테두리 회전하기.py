def solution(rows, columns, queries):
    answer = []
    mat = [[columns*row+col+1 for col in range(columns)] for row in range(rows)]

    for x1,y1,x2,y2 in queries:
        start = mat[x1-1][y1-1]
        mini = start

        for k in range(x1-1,x2-1): # 7 to 11
            end = mat[k+1][y1-1]
            mat[k][y1-1] = end
            if mini>end: mini = end

        for k in range(y1-1,y2-1): # 11 to 1
            end = mat[x2-1][k+1]
            mat[x2-1][k] = end
            mini = min(mini, end)

        for k in range(x2-1,x1-1,-1): # 1 to 5
            end = mat[k-1][y2-1]
            mat[k][y2-1] = end
            mini = min(mini, end)

        for k in range(y2-1,y1-1,-1): # 5 to 7
            end = mat[x1-1][k-1]
            mat[x1-1][k] = end
            mini = min(mini, end)

        mat[x1-1][y1] = start
        answer.append(mini)

    return answer