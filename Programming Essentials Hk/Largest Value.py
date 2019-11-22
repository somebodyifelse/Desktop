#This program belongs to determine the largest value.....

print('#This program belongs to determine the largest value....');

print('\nStart>>>\n')
a = str(input('a: '));
b = str(input('b: '));
c = str(input('c: '));

if a>b and a>c:
    print('Largest Value is a = %c'%a)
elif b>a and b>c:
    print('Largest Value is b.')
elif c>a and c>b:
    print('Largest Value is c.')
else:
    print('All the Numbers are Equal.')
    

print('<<<End');
