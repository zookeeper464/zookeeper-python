import re

s = input()
word = input()
#입력값 입력

p = re.compile(word)
answer = p.findall(s)
#정규식 처리

print(len(answer))
