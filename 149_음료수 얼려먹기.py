row, col = map(int, input().split())
li = []
for i in range(row):
    li.append(list(map(int, input())))

visited = [[False for _ in range(col)] for _ in range(row)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(r, c):
    if r < 0 or r >= row or c < 0 or c >= col:
        return
    if visited[r][c] or li[r][c] != 0:
        return
    
    visited[r][c] = True
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        dfs(nr, nc)

cnt = 0
for r in range(row):
    for c in range(col):
        if li[r][c] == 0 and not visited[r][c]:
            cnt += 1
            dfs(r, c)
            
print(visited[0])
print(visited[1])
print(visited[2])
print(visited[3])
print(cnt)
