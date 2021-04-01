s = input()

if s[0] == "F":
  print(0.0)
  #F이면 낙제
 
else:
  answer = 69 - ord(s[0])
  #A,B,C,D구분
  
  if s[1] == "+":
    answer += 0.3
  elif s[1] == "-":
    answer -= 0.3
  else:
    answer += 0.0
    #+,0,-구분
    
  print(answer)
