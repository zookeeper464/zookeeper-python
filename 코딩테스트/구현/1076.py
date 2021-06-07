lst = ["black", "brown", "red", "orange", "yellow","green","blue","violet",'grey','white']

answer = 0
answer += lst.index(input())*10
answer += lst.index(input())
answer *= 10**(lst.index(input()))
print(answer)
