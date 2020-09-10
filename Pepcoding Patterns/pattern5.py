n = int(input())
spaces = n // 2
stars = 1

for i in range(1, n+1):
    for j in range(1, spaces+1):
        print('\t')
    for j in range(1, stars+1):
        print('*\t')
    if i <= n // 2:
        spaces -= 1
        stars += 2
    else:
        spaces += 1
        stars -= 2
    print()