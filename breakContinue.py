""" wynik = 0

for i in range(23):
    x = int(input('Podaj dodatnią liczbe: '))
    if (x > 0):
        wynik += x
    else:
        print('Miała być liczba dodatnia !! Game Over !')
        break
    print("Aktualny wynik dodawania to", wynik)
"""
wynik = 0
 
i = 0

while i < 3:
    x = int(input('Podaj dodatnią liczbe parzystą: '))
    if (x % 2 == 0) and (x > 0):
        wynik += x
    elif (x % 2 == 0) and (x < 0):
        print('Twoja liczba jest parzysta, ale nie jest dodatnia !! Sprobuj jeszcze raz')
        continue
    elif (x % 2 != 0) and (x > 0):
        print('Liczba', x, 'nie jest liczbą parzystą !, Sprobuj jeszcze raz')
        continue
    else: 
        print('Liczba', x, 'nie jest ani parzysta ani dodatnia. Na Boga, ogarnij sie i sprobuj jeszcze raz')
        continue
    print("Aktualny wynik dodawania liczb parzystych to", wynik)
    i += 1