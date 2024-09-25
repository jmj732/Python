count = 0
charge = [500,100,50,10]
n=int(input())

for c in charge:
    if n >= c:
        count += n // c
        n %= c 
print(count)