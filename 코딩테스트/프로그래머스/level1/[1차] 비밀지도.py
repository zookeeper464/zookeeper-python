def solution(n, arr1, arr2):
    answer = ['']*n
    arr = [arr1[i]|arr2[i] for i in range(n)]
    for idx,r in enumerate(arr):
        for i in range(n):
            if (r>>(n-1-i))%2:
                answer[idx] += '#'
            else:
                answer[idx] += ' '
    return answer