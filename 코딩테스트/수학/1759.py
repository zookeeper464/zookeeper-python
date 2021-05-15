l,c = map(int,input().split())
s = input().split()
s.sort()
#입력

answer =["" for i in range(l)]
def dfs (start,depth):
  answer[depth] = s[start]
  #조건 삽입

  ae = len(set(answer)&set(["a","e","i","o","u"]))
  if depth == l-1 and ae>0 and l-ae>1:
    print("".join(answer))
    return
  #조건에 맞는지 판별

  for i in range(start+1,len(s)):
    dfs(i,depth+1)
  #다음 단계 진행

for i in range(len(s)-l+1):
  dfs(i,0)
#처음 시작 실행
