firstTime = True
while True:
    print('Is ranining?')
    rain = input()
    if rain == 'yes':
        if firstTime:
            firstTime=False
            print('Have umbrella?')
            umb = input()
            if umb == 'yes':
                break
            else:
                print('Wait a while.')
    else:
        break
print('Go outside')
