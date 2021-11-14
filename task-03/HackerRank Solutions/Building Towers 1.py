n = int(input())
r = list(map(int,input().split()))
b =  len(set(r))
max_occuring = max(r,key=r.count)
a = 0
for i in range(n):
    if max_occuring == r[i]:
        a = a + 1
print (a,b, sep=" ")
