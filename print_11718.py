import sys
input = sys.stdin.readlines
#줄 바꿈을 모두 받으며, 줄바꿈마다 다른 인덱스로 하여 받는 리스트 생성

temp = input()
print("".join(temp))
