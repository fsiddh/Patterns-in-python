for rows in range(5, 0, -1):
    for spaces in range(0, rows-1):
        print('', end=' ')
    for asterisk in range(0, 6-rows):
        print('*', end=' ') 
    print()