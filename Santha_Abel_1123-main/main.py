from os import system
from functions import *

choice=''
while choice!='0':
    system('cls')
    choice=menu()
    if choice=='1':
        system('cls')
        while jatek:
            printtabla(tabla)
            bekeres(tabla)
            csekk_nyertes(tabla)
            csekk_dontetlen(tabla)
            karakter_csere()
            bot(tabla)
            csekk_nyertes(tabla)
            csekk_dontetlen(tabla)
    elif choice=='2':
        system('cls')
        ko_papir_ollo()
    elif choice=='3':
        system('cls')
        szamkitalalos()
        rekordok_betoltese()
    elif choice=='4':
        system('cls')
        rekordok_choice = ''
        while rekordok_choice!='0':
            system('cls')
            rekordok_choice = rekordok()
            if rekordok_choice=='0':
                system('cls')
            elif rekordok_choice=='1':
                system('cls')
                osszes_rekordok_kilistazasa()
            elif rekordok_choice=='2':
                system('cls')
                #legjobb_rekord_kilistazasa()
