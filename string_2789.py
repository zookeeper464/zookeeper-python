import re
lst = list('CAMBRIDGE')
p = re.compile(f"{lst}")
s = input()
#캠브리지 정규식 생성, 입력값 입력
answer = p.sub('', s)
#해당 문자 제거
print(answer)
