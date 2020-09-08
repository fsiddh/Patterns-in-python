horizontal_mid = 2
vertical_mid = 2

for i in range(5):
    for j in range(5):
        if i == horizontal_mid or j == vertical_mid:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()    