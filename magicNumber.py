szukanaLiczba = 40
zgadywanaLiczba = 0
while zgadywanaLiczba != szukanaLiczba:
    zgadywanaLiczba = int(input('Odganij o jaka liczbe mi chodzi: '))

    if (zgadywanaLiczba < szukanaLiczba):
        print('Twoja liczba jest mniejsza od poszukiwanej')

    elif (zgadywanaLiczba > szukanaLiczba):
        print('Twoja liczba jest wieksza od poszukiwanej')

    else:
        print:('BRAWO')
