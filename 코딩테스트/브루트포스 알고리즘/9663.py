n = int(input())
answer = 0

row, right, left = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def dfs(i):
  global answer
  if i == n:
    answer += 1
    return

  for j in range(n):
    if (not row[j] and not right[i+j] and not left[i+(n-1-j)]) :
      row[j] = right[i+j] = left[i-j+n-1] = True
      dfs(i+1)
      row[j] = right[i+j] = left[i+(n-1-j)] = False

dfs(0)
print(answer)
