name = str(input('Enter your name: '))

if (name=='Alice' or name == 'alice'):
        print('Hi, Alice.\n')
else:
        age = int(input('Enter your Age: '))
        if age < 12:
                print('You are not Alice, Kiddo.\n')
        elif age > 2000:
                print('Unlike you, Alice is not undead, immortal vampire.\n')
        elif age > 100:
                print('You are not Alice, Grannie.\n')

