from sys import stdin

def input():
  return stdin.readline().rstrip('\n')

N,M = [int(x) for x in input().split(" ")]
input_list = input().split(" ")
input_list.sort(key=lambda x : int(x))
answer_list = []
temp_list = []

def ranked_comb(num):
  global answer_list, input_list, temp_list, M
  
  if (num == M):
    answer_list.append(" ".join(temp_list))
    return 
  
  for i in range(len(input_list)):
    temp_list.append(input_list[i])
    ranked_comb(num+1)
    temp_list.pop()
                  
ranked_comb(0)

print(*answer_list,sep='\n')
