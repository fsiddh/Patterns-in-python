x = int(input())

for i in range(1, x+1):
    for j in range(0, x):
        if j < x-i or j > x-i:
            print('', end='\t')
        else:
            print('*', end='\t')
    print()