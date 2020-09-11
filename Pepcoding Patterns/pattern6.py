n = int(input())
stars = n // 2 +1
spaces = 1

for i in range(0, n):
    for ls in range(0, stars):
        print('*\t', end='')
    for sp in range(0, spaces):
        print('\t', end='')
    for rs in range(0, stars):
        print('*\t', end='')
    
    if i < n//2:
        stars -= 1
        spaces += 2
    else:
        stars += 1
        spaces -= 2
    print()