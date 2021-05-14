#필요한 입력값 입력
v_lst, lst=[], []
while True:
  l = list(map(int,input().split()))
  if l==[0]:
    break
  v_lst.append(l[0])
  lst.append(l[1:])

#데이터 처리를 위한 함수 설정
answer=[0,0,0,0,0,0]
def DFS(start,depth,lst,l,answer):
  if depth==6:
    print(" ".join(list(map(str,answer))))
    return
    #6번째 칸이 채워지면 출력

  if start > len(lst)-6+depth:
    return
    #6번째 칸이 채워질 수 없는 경우 탈출

  for i in range(start,l):
    answer[depth]=lst[i]
    DFS(i+1,depth+1,lst,l,answer)
    #다음 칸에 대한 함수 시작

#
n=len(v_lst)
for i in range(n):
  DFS(0,0,lst[i],v_lst[i],answer)
  print()
