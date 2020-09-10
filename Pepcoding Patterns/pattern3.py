x = int(input())

for i in range(1, x+1):
    for spaces in range(0, x-i):
        print('', end='	')
    for asterisk in range(0, i):
        print('*', end='	')
    print()