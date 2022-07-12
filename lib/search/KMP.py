def KMP(string,pattern):
  rank,i = [0]*len(pattern),0
  
  for j in range(1,len(pattern)):
    while (i>0 and pattern[i] != pattern[j]):
      i = rank[i-1]
      
    if (pattern[i] == pattern[j]):
      i += 1
      rank[j] = i
    
  result = []
  i = 0
  for j in range(len(string)):
    while (i>0 and pattern[i] != string[j]):
      i = rank[i-1]
      
    if (pattern[i] == string[j]):
      i += 1
      if i == len(pattern):
        result.append(j-i+1)
        i = rank[i-1]
        
  return result
