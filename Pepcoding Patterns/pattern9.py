x = int(input())

for i in range(0, x):
    for j in range(0, x):
        if j == i or j == ((x-1)-i):
            print('*', end='\t')
        else:
            print('', end='\t')
    print()