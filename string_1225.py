n, m = map(list,input().split())
#입력값을 받아 리스트로 변형

n, m = map(int,n), map(int,m)
#변형한 리스트의 내용을 정수로 변환


print(sum(n)*sum(m))
