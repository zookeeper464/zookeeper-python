import sys
input = sys.stdin.readline

word=input()
answer=0

def check(word):
  global answer
  stack=[]
  temp=1
  for i in range(len(word)):
    if word[i]=="(": 
      stack.append(2)
    elif word[i]=="[":
      stack.append(3)  
    elif word[i]==")" and stack!=[]:
      if stack[-1]==2:
        if word[i-1]=="(":
          for j in stack:
            temp*=j
          answer+=temp
          temp=1
        stack.pop()
      else:
        return False
    elif word[i]=="]" and stack!=[]:
      if stack[-1]==3:
        if word[i-1]=="[":
          for j in stack:
            temp*=j
          answer+=temp
          temp=1
        stack.pop()
      else:
        return False
    elif word[i]=="\n" and stack==[]:
      return True
    else:
      return False
  if stack==[]:
    return True
  else:
    return False

if check(word):
  print(answer)
else:
  print(0)
