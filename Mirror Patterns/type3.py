for i in range(-4, 5):
    for j in range(0, 5):
        if (j == abs(i)) or j == (4-abs(i)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()