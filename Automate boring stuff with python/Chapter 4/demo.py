cat1 = 'Zophie'
cat2 = 'Pooka'
cat3 = 'Simon'
cat4 = 'Lady Macbeth'
cat5 = 'Fat-tail'


cats = []
while True:
        print('Enter the name of cat ' + str(len(cats) + 1)+'(or enter nothing to stop.):')
        name = input()
        if name == '':
                break
        cats = cats + [name]
print('The cat names are:')
for name in cats:
        print(' '+name)
