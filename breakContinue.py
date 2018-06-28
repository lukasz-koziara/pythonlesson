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
    x = int(input('Podaj dodatnią liczbe: '))
    if (x > 0):
        wynik += x
    else:
        print('Miała być liczba dodatnia !! Sprobuj jeszcze raz')
        continue
    print("Aktualny wynik dodawania to", wynik)
    i += 1