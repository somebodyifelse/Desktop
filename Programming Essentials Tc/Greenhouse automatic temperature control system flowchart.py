print('>>>Start')
Temperature = input('Is Temperature <20 Degree: ')
if (Temperature == 'Yes' or Temperature=='yes'):
        print('Turn Heater on')
        greaterthan_23= input('Is Temperature > 23 Degree: ')
        if (greaterthan_23 == 'Yes' or greaterthan_23 == 'yes' or greaterthan_23 == 'hmm'):
                print('Turn Heater Off')
        else:
                print('Let it go as it is')
        
else:
        print('Let it go as it is')
print('End')
