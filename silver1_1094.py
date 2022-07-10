from sys import stdin

def input():
  return stdin.readline().rstrip('\n')

size,row,col = input().split(" ")
num = 1<<int(size)
row,col = int(row),int(col)

answer = 0
while (num!=1):
  num = num>>1
  if num<=row:
    answer += 2*num**2
    row -= num
  if num<=col:
    answer += num**2
    col -= num

print(answer)
