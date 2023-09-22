for i in range(1, 11):

    for j in range(1, i + 1):
        print('*', end='')
    print('   ', end='')


    for j in range(10, i, -1):
        print('*', end='')
    print('   ', end='')


    for j in range(1, 11 - i):
        print(' ', end='')
    for j in range(1, i + 1):
        print('*', end='')
    print('   ', end='')

    
    for j in range(1, i):
        print(' ', end='')
    for j in range(i, 11):
        print('*', end='')
    print()

