row = 7
col = 7
li = []
for i in range(row):
    li.append(list(map(int, input().split())))

visited = [[False for _ in range(col)] for _ in range(row)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(r, c, color):
    if r < 0 or r >= row or c < 0 or c >= col:
        return 0
    if visited[r][c] or li[r][c] != color:
        return 0
    
    visited[r][c] = True
    size = 1
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        size += dfs(nr, nc, color)
        
    return size

area = 0
for k in range(1,6):
    color = k
    for r in range(row):
        for c in range(col):
            if li[r][c] == color and not visited[r][c]:
                size = dfs(r, c, color)
                if size >= 3:  
                    area += 1

print(area)
