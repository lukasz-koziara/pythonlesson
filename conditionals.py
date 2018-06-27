wybor = input('1 - mnozenie, 2 - dzielenie, 3 - dodawanie, 4 - odejmowanie ')

a = int(input('Pierwsza liczba '))
b = int(input('Druga liczba '))

if (wybor == "1"):
    print('Wynik a * b =',a * b)
elif(wybor == "2"):
    if (b == 0):
        print('Error, autodestruction in 5 sec (Cholero nie dziel przez zero)')
    else:
        print('Wynik a / b =',a / b)
elif(wybor == "3"):
    print('Wynik a + b =',a + b)
elif(wybor == "4"):
    print('Wynik a - b =',a - b)
else:
    print('Nie bangla !')
