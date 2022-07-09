answer_list = []
input_list = []
temp_list = []
N = 0

def nonrepeats_comb(num):
  global answer_list, input_list, temp_list, N
  
  if (num == N):
    answer_list.append(" ".join(map(lambda x : input_list[x],temp_list)))
    return 
  
  for i in range(N):
    if (i not in temp_list):
      temp_list.append(i)
      nonrepeats_comb(num+1)
      temp_list.pop()
                  
nonrepeats_comb(0)
