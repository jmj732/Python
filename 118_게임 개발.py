dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
sx, sy, direction = map(int, input().split())  
path = [[0] * m for _ in range(n)]
path[sy][sx] = 1

mymap = []
for i in range(n):
    row = list(map(int, input().split()))
    mymap.append(row)

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 0
turn_time = 0
while True:
    turn_left()
    ny = sy + dy[direction]
    nx = sx + dx[direction]
    if path[ny][nx] == 0 and mymap[ny][nx] == 0:
        sx = nx
        sy = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = sx - dx[direction]
        ny = sy - dy[direction]
        if mymap[ny][nx] == 0:
            sx = nx
            sy = ny
        else:
            break
        turn_time = 0
print(count)