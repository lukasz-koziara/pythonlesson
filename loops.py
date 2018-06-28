wynik = 0
for i in range(100):
    if (i % 6 == 0) and (i % 4 != 0):
        print('Liczba', i, ' jest podzielna przez 6, ale nie jest podzielna przez 4')
    elif (i % 6 != 0) and (i % 4 == 0): 
        print('Liczba', i, ' nie jest podzielna przez 6, ale jest podzielna przez 4')
    elif (i % 6 == 0) and (i % 4 == 0):
        print('Liczba', i, ' jest podzielna przez 6 i przez 4')
    else:
        print('Liczba', i, 'nie dzieli sie przez 4 ani przez 6')