from sys import stdin

input = stdin.readline

N = int(input())
def main (N):
    if N in (1,3):
        return -1
    
    answer = 0
    if N%2:
        answer += 1
        N-=5
    
    answer += 2*(N//10)
    N %=10
    answer += N//2
    return answer

print(main(N))
