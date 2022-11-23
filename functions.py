from os import system
from random import randint

def menu():
    print('JÁTÉKOK')
    print('0 - Kilépés')
    print('1 - Amőba')
    print('2 - Kő-papír-olló')
    print('3 - Találd ki a számot')
    print('4 - Rekordok')
    choice=input('Válasszon egy menüpontot: ')
    return choice

def szamkitalalos():

    min_szam = 0
    max_szam = 0
    min_szam = int(input('Az intervallum legkisebb értékét adja meg!\n'))
    while max_szam < min_szam:
        max_szam = int(input('Adjon meg az előző számnál nagyobb értéket!\n'))

    random_szam=randint(min_szam,max_szam)




    print('Kezdődhet a tippelés 0 és 100 között!\n')
    tipp=int(input(''))
    while tipp != random_szam:
        if tipp > random_szam:
            system('cls')
            tipp = int(input('Kisebbet próbálj!\n'))
        else:
            system('cls')
            tipp = int(input('Nagyobbat próbálj!\n'))

    input(f'Gratulálok, kitaláltad! A szám: {random_szam} volt')
