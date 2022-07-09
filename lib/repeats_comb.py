answer_list = []
input_list = []
temp_list = []
N = 0

def repeats_comb(num):
  global answer_list, input_list, temp_list, N
  
  if (num == N):
    answer_list.append(" ".join(temp_list)
    return 
  
  for i in input_list:
    temp_list.append(i)
    repeats_comb(num+1)
    temp_list.pop()
                  
repeats_comb(0)
