x = int(input())

for i in range(0, x):
    for spaces in range(0, i):
        print('', end='	')
    for asterisk in range(0, x-i):
        print('*', end='	')
    print()