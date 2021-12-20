def solution(arr1, arr2):
    n, m ,k = len(arr1), len(arr2), len(arr2[0])
    answer = [[sum([arr1[i][l]*arr2[l][j] for l in range(m)]) for j in range(k)] for i in range(n)]
        
    return answer