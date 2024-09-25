place = input().strip()
count = 0
steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

pC = ord(place[0]) - ord('a') + 1
cR = int(place[1])



for step in steps:
    if 1 <= pC + step[0] <= 8 and 1 <= cR + step[1] <= 8:
            count += 1
print(count)
