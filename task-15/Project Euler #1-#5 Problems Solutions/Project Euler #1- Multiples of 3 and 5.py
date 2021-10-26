def sum(x):
    result = x*(x+1)//2
    return result
T = int(input())
for i in range(T):
    N = int(input())
    a = (N-1) // 3
    b = (N-1) // 5
    c = (N-1) // 15
    print(3*sum(a) + 5*sum(b) - 15*sum(c))
    #python3 solution
