p = int(input())
answer = []

def fibo (num):
    lst = [1,1]
    while True:
        lst.append((lst[-1]+lst[-2])%num)
        if lst[-1] == 0 and lst[-2] == 1:
            return len(lst)

for _ in range(p):
    n,m = map(int,input().split())
    answer.append(f'{n} {fibo(m)}')

print('\n'.join(answer))
