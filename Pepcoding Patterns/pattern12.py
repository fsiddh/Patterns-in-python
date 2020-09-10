fibo_storage = {}
def fibo(n):
    if n in fibo_storage:
        return fibo_storage[n]
    if n == 0 or n == 1:
        value = n
    else:
        value = fibo(n-2) + fibo(n-1)
    fibo_storage[n] = value
    return value

for i in range(20):
    fibo(i)

x = int(input())
t = 0

for i in range(0, x):
    for j in range(0, i+1):
        print(fibo_storage[t], end='\t')
        t += 1
    print()