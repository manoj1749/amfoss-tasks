p = []
for i in range(100,999):
    for j in range(100,999):
        if str(i*j) == str(i*j)[::-1]:
            p.append(i*j)
t = int(input())
for i in range(t):
    pi = []
    n = int(input())
    for i in p:
        if i < n:
            pi.append(i)
    print(max(pi))
