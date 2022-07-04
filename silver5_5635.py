from sys import stdin

input = stdin.readline

N = int(input())
old = ["",20110101]
young = ["",19890101]
for _ in range(N):
    temp = input().rstrip("\n").split(" ")
    birthdate = temp[3]
    if len(temp[2])==1: birthdate+= "0"
    birthdate += temp[2]
    if len(temp[1])==1: birthdate+= "0"
    birthdate += temp[1]
    birthdate = int(birthdate)
    if (birthdate<old[1]):
        old = [temp[0],birthdate]
    if (birthdate>young[1]):
        young = [temp[0],birthdate]

print(young[0])
print(old[0])
