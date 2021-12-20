def solution(n, left, right):
    l = right - left
    start = left%n
    end = start+l+1
    answer = sum([[c+1 if r<=c else r+1 for c in range(n)] for r in range(int(left/n),int(right/n)+1)],[])[start:end]
    return answer