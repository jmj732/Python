n,m,k = map(int,input().split())
li = list(map(int,input().split()))
li.sort()

B = li[-1]
S = li[-2]

sum = 0

while m != 0:
    if m > k :
        for i in range(k):
            sum += B
        sum += S
        m -= k+1
    else:
        for i in range(m % k):
            sum += B
        m = 0
print(sum)