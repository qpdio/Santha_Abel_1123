from os import system
from random import randint
from data import szamkitalalos, kopapirollo, amoba, szamkitalalos_rekord

szamkitalalos_file_name='rekord_szamkitalalos.csv'
kopapirollo_file_name='rekord_kopapirollo.csv'
amoba_file_name='rekord_amoba.csv'

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
    tippek_szama = 0
    min_szam = int(input('Az intervallum legkisebb értékét adja meg!\n'))
    while max_szam < min_szam:
        max_szam = int(input('Adjon meg az előző számnál nagyobb értéket!\n'))

    random_szam=randint(min_szam,max_szam)

    print(f'Kezdődhet a tippelés {min_szam} és {max_szam} között!\n')
    tipp=int(input(''))
    while tipp != random_szam:
        if tipp > random_szam:
            system('cls')
            tipp = int(input('Kisebbet próbálj!\n'))
            tippek_szama += 1
        else:
            system('cls')
            tipp = int(input('Nagyobbat próbálj!\n'))
            tippek_szama += 1
    tippek_szama_mentese_fajlba(tippek_szama)
    input(f'Gratulálok, kitaláltad! A szám: {random_szam} volt.\n{tippek_szama+1} lépésből sikerült kitalálnod a számot.')



def tippek_szama_mentese_fajlba(tippek_szama):
    file=open(szamkitalalos_file_name, 'a', encoding='utf-8')
    file.write(f'\n{tippek_szama+1}')

def rekordok():
    print('0 - Vissza')
    print('1 - Összes rekord')
    print('2 - Legjobb rekord')
    rekord_choice = input('Válasszon egy menüpontot: ')
    return rekord_choice
    
    
def rekordok_betoltese():
    file=open(szamkitalalos_file_name, 'r', encoding='utf-8')
    file.readline()
    for egysor in file:
        egysor.strip()          
        szamkitalalos_rekord.append(int(egysor))
    file.close()
    
def osszes_rekordok_kilistazasa():
    print('Rekordjaid:')
    for i in range(len(szamkitalalos_rekord)):
        print(f'{i}. {szamkitalalos_rekord[i]}')
    input('Tovább...')
    
