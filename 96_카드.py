n,m = map(int,input().split())
smli = []
li = []

for i in range(n):
    li = list(map(int,input().split()))
    li.sort()
    smli.append(li[0])
    
smli.sort()

print(smli[-1])