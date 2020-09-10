for i in range(0, 5):
    for j in range(0, 5):
        if j == i or j == (4-i):
            print('*', end='\t')
        else:
            print('', end='\t')
    print()