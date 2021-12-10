def solution(sizes):
    row,col = [],[]
    for a,b in sizes:
        if a>b: row.append(a); col.append(b)
        else: row.append(b); col.append(a)
    
    answer = max(row)*max(col)
    return answer