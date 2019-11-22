print('#Here, we set up this program for infinity to Determine the "Gram" value from Kiogram,Quintal and Metricton. If you want, you can add more program......."Thank You"')

while True:
            print('>>>Pls enter the value with "Extension". Like: Kilogram = Kg, Quintal = Qt, Metricton = Mt\n')
            a = float(input('Enter your value: '))
            b = str(input('Must:- Enter the "Extension": '))
            if (b == 'kg' or b == 'Kg' or b== 'KG' or b== 'kG'):
                        c = a*1000    #1Kg = 1000Gram
                        print(a,'Kilogram = ',c,'Gram\n\n')
            elif (b == 'Qt' or b == 'qt' or b == 'QT' or b == 'qT'):
                        c = a*100*1000    #1 Quintal = 100Kg
                        print(a,'Quintal = ',c,'Gram\n\n')
            else:
                        print('Pls enter the Valid Integer or "Extension"')
                        
