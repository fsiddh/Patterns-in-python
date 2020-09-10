x = int(input())

for i in range(0, x):
    for j in range(x-i, 0, -1):
        print('*', end='	')
    print()