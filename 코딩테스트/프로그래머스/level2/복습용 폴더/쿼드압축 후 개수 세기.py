def solution(arr):
    def compression(r,c,l):
        nonlocal answer
        
        start = arr[r][c]
        for i in range(r,r+l):
            for j in range(c,c+l):
                if arr[i][j] == start:
                    continue
                    
                l //= 2
                compression(r,c,l)
                compression(r,c+l,l)
                compression(r+l,c,l)
                compression(r+l,c+l,l)
                return
                
        answer[start]+=1
        
    answer=[0,0]
    l = len(arr)
        
    compression(0,0,l)
    
    return (answer)