n = int(input())
spaces = n // 2
stars = 1

for i in range(0, n):
    for sp in range(0, spaces):
        print('\t', end='')
    for st in range(0, stars):
        print('*\t', end='')
    print()

    if i < n//2:
        spaces -= 1
        stars += 2
    else:
        spaces += 1
        stars -= 2