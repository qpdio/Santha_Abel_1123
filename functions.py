from os import system
from random import randint
from data import szamkitalalos, kopapirollo, amoba, szamkitalalos_rekord
from random import randint

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
    
def ko_papir_ollo():

    opciok = ['kő', 'papír', 'olló']
    valasztas = ''
    random_szam = randint(0,2)
    bot_valasztas = opciok[random_szam]
    pontok = 0

    print('kő - papír - olló?')

    while valasztas not in opciok:
        valasztas = input('Válassz!\n')
    
    system('cls')

    if valasztas == 'kő' and bot_valasztas == 'papír':
        print('Nyertél')
        pontok += 1
        print(f'A gép a következőt választotta: {bot_valasztas}')
        pontok_mentese_fajlba(pontok)
    elif valasztas == 'papír' and bot_valasztas == 'olló':
        print('Nyertél')
        pontok += 1
        print(f'A gép a következőt választotta: {bot_valasztas}')
        pontok_mentese_fajlba(pontok)
    elif valasztas == 'olló' and bot_valasztas == 'papír':
        print('Nyertél')
        pontok += 1
        print(f'A gép a következőt választotta: {bot_valasztas}')
        pontok_mentese_fajlba(pontok)
    else:
        if valasztas == bot_valasztas:
            print('Döntetlen')
            print(f'A gép a következőt választotta: {bot_valasztas}')
        else:
            print('Vesztettél')
            print(f'A gép a következőt választotta: {bot_valasztas}')
            pontok -= 1
            pontok_mentese_fajlba(pontok)
    

    input('')
    system('cls')
    jatek_ujra = input('Szeretnél újra játszani? Igen / Nem\n').lower()

    if jatek_ujra == 'igen' or jatek_ujra != 'nem':
        system('cls')
        ko_papir_ollo()
    else:
        system('cls')
        input('Tovább...')
    
    

def pontok_mentese_fajlba(pontok):
    file=open(kopapirollo_file_name, 'a', encoding='utf-8')
    file.write(f'\n{pontok}')
