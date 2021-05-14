e,s,m = map(int,input().split())

answer = 0
answer += 28*19*e*13
answer += 15*19*s*17
answer += 15*28*m*10
answer = (answer-1)%(15*28*19)+1
print(answer)
