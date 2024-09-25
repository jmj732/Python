x = 1
y = 1
n = int(input())
li = input().split()
for mv in li:
    if mv == 'L' and x - 1  >= 1 :
        x -= 1
    elif mv == 'R' and x + 1 <= n:
        x += 1
    elif mv == 'U' and y - 1 >= 1:
        y -= 1
    elif mv == 'D' and y + 1 <= n:
        y += 1
print(y, x)
