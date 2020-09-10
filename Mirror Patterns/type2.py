for i in range(-3, 4):
    for spaces in range(0, abs(i)):
        print(' ', end='\t')
    for asterisk in range(0, 4-abs(i)):
        print('*\t', end='\t')
    print()