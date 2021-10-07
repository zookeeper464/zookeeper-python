from math import log

star = ['  *   ',' * *  ','***** ']
n = int(input())
answer = ''  

def add_star():
  for i in range(len(star)):
    star.append(star[i]*2)

def half_rshift(num):
  for i in range(len(star)//2):
    star[i] = ' '*(3*2**num)+star[i]+' '*(3*2**num)

for num in range(int(log(n,2))-1):
  add_star()
  half_rshift(num)

print(*star, sep='\n')
