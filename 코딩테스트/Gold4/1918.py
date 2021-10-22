n = list(input())
oper_dict = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}

postfix = []
stack = []
ans= ''

for i in n:
  if 'A' <= i <= 'Z':
    postfix.append(i)
  elif i == '(':
    stack.append(i)
    
  elif i == ')':
    while stack[-1] != '(':
      postfix.append(stack.pop())
    stack.pop()

  else:
    while stack and oper_dict[i] <= oper_dict[stack[-1]]:
      postfix.append(stack.pop())
    stack.append(i)
        
while len(stack) != 0:
  postfix.append(stack.pop())
    
print(''.join(postfix))
