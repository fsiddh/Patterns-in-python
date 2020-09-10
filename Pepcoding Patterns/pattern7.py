x = int(input())

for i in range(0, x):
    for j in range(0, i+1):
        if j == i:
            print('*', end='\t')
        else:
            print('', end='\t')
    print()