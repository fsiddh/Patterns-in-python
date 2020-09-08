for rows in range(5, 0, -1):
    for spaces in range(0, 5-rows):
        print(' ', end=' ')
    for asterisk in range(0, rows):
        print('*', end=' ')
    print()