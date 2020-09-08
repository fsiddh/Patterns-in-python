spaces = 0
for i in range(0, 5):
    for j in range(0, 5):
        if j == spaces:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    spaces += 1