from os import system
from data import szamkitalalos, kopapirollo, amoba, szamkitalalos_rekord
import random
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
    
    
def rekordok_betoltese_szamkitalalos():
    file=open(szamkitalalos_file_name, 'r', encoding='utf-8')
    file.readline()
    for egysor in file:
        egysor.strip()          
        szamkitalalos_rekord.append(int(egysor))
    file.close()

def rekordok_betoltese_kopapirollo():
    file=open(kopapirollo_file_name, 'r', encoding='utf-8')
    file.readline()
    for egysor in file:
        egysor.strip()          
        kopapirollo.append(int(egysor))
    file.close()
    
def osszes_rekordok_kilistazasa_szamkitalalos():
    print('Rekordjaid [Számkitalálós]:')
    for i in range(len(szamkitalalos_rekord)):
        print(f'{i}. {szamkitalalos_rekord[i]}')

    input('Tovább...')

def osszes_rekordok_kilistazasa_kopapirollo():
    print('Pontjaid [Kő-papír-olló]:')
    pontjaim = 0
    for i in range(len(kopapirollo)):
        pontjaim += kopapirollo[i]
    print(f'{pontjaim}')

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
    
    

def pontok_mentese_fajlba(pontok):
    file=open(kopapirollo_file_name, 'a', encoding='utf-8')
    file.write(f'\n{pontok}')


tabla = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
jelenlegi_jatekos = "X"
nyertes = None
jatek = True

def printtabla(tabla):
    print(tabla[0] + " | " + tabla[1] + " | " + tabla[2])
    print("---------")
    print(tabla[3] + " | " + tabla[4] + " | " + tabla[5])
    print("---------")
    print(tabla[6] + " | " + tabla[7] + " | " + tabla[8])



def bekeres(tabla):
    inp = int(input("Válassz egy helyet 1-től 9-ig: "))
    if tabla[inp-1] == "-":
        tabla[inp-1] = jelenlegi_jatekos
    else:
        print("Nem választató!")


def csekk_vizszintesen(tabla):
    global nyertes
    if tabla[0] == tabla[1] == tabla[2] and tabla[0] != "-":
        nyertes = tabla[0]
        return True
    elif tabla[3] == tabla[4] == tabla[5] and tabla[3] != "-":
        nyertes = tabla[3]
        return True
    elif tabla[6] == tabla[7] == tabla[8] and tabla[6] != "-":
        nyertes = tabla[6]
        return True

def csekk_oszloposan(tabla):
    global nyertes
    if tabla[0] == tabla[3] == tabla[6] and tabla[0] != "-":
        nyertes = tabla[0]
        return True
    elif tabla[1] == tabla[4] == tabla[7] and tabla[1] != "-":
        nyertes = tabla[1]
        return True
    elif tabla[2] == tabla[5] == tabla[8] and tabla[2] != "-":
        nyertes = tabla[3]
        return True


def csekk_atlosan(tabla):
    global nyertes
    if tabla[0] == tabla[4] == tabla[8] and tabla[0] != "-":
        nyertes = tabla[0]
        return True
    elif tabla[2] == tabla[4] == tabla[6] and tabla[4] != "-":
        nyertes = tabla[2]
        return True


def csekk_nyertes(tabla):
    global jatek
    if csekk_vizszintesen(tabla):
        printtabla(tabla)
        print(f"A nyertes: {nyertes}!")
        jatek = False

    elif csekk_oszloposan(tabla):
        printtabla(tabla)
        print(f"A nyertes: {nyertes}!")
        jatek = False

    elif csekk_atlosan(tabla):
        printtabla(tabla)
        print(f"A nyertes: {nyertes}!")
        jatek = False


def csekk_dontetlen(tabla):
    global jatek
    if "-" not in tabla:
        printtabla(tabla)
        print("Döntetlen!")
        jatek = False


def karakter_csere():
    global jelenlegi_jatekos
    if jelenlegi_jatekos == "X":
        jelenlegi_jatekos = "O"
    else:
        jelenlegi_jatekos = "X"


def bot(tabla):
    while jelenlegi_jatekos == "O":
        pozicio = random.randint(0, 8)
        if tabla[pozicio] == "-":
            tabla[pozicio] = "O"
            karakter_csere()

while jatek:
            printtabla(tabla)
            bekeres(tabla)
            csekk_nyertes(tabla)
            csekk_dontetlen(tabla)
            karakter_csere()
            bot(tabla)
            csekk_nyertes(tabla)
            csekk_dontetlen(tabla)


def rekordok_osszes():
    print('0 - Vissza')
    print('1 - Összes számkitalálós rekord listázása')
    print('2 - Összes kő-papír-olló rekord listázása')
    rekord_choice = input('Válasszon egy menüpontot: ')
    return rekord_choice

def legjobb_rekord_kilistazasa():
    
    for i in range(len(kopapirollo)):
        if i > kopapirollo[i]:
            i = kopapirollo[i]
    print('Szamkitalálós játékban legjobb rekordod: ')
    print(i+2)
    input('Tovább...')
