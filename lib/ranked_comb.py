answer_list = []
input_list = []
temp_list = []
N = 0
input_list.sort()

def ranked_comb(num,idx):
  global answer_list, input_list, temp_list, N
  
  if (num == N):
    answer_list.append(" ".join(temp_list))
    return 
  
  for i in range(idx+1,len(input_list)):
    temp_list.append(input_list[i])
    ranked_comb(num+1,i)
    temp_list.pop()
                  
ranked_comb(0,-1)
