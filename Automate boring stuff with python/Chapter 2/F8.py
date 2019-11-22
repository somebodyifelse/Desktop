name = str(input('Enter your name: '))

if (name=='Alice' or name=='alice'):
        print('Hi, Alice.\n')
else:
        age = int(input('Enter your age: '))
        if age < 12:
                print('\nYou are not Alice, Kiddo.\n')
        else:
                print('\nYou are neither Alice nor a little kid.\n')


