allguests = {'Alice':{'apple': '5', 'orange': '6'},
             'Arafat': {'apple': '4', 'orange': '8'}}
def totalbrought(guests, item):
        numbrought = 0
        for k, v in guests.items():
                numbrought = numbrought + v.get(item, 0)
        return numbrought
print('Number of things being brought: ')
print(' - Apples ' + str(totalbrought(allguests, 'apple')))
print(' - Orange ' + str(totalbrought(allguests, 'orange')))
